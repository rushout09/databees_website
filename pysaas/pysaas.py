'''

pysaas.py

This file contains:
    1. The app state classes, variables, and methods.
    2. The app page routes, metadata, and webhook listener.

'''

import reflex as rx
import pandas as pd
import yfinance as yf
import requests
import pyrebase
import json
import os
import hashlib
import hmac
from typing import Optional
from email_validator import validate_email
from fastapi import Request, HTTPException
from dateutil import parser
from dotenv import load_dotenv

from rxconfig import config
from pysaas.components.post import Post, PostSectionContent
from pysaas.pages.index import index
from pysaas.pages.blog import blog, post
from pysaas.pages.signin import signin
from pysaas.pages.signup import signup
from pysaas.pages.signout import signout
from pysaas.pages.dashboard import dashboard
from pysaas.pages.notfound import not_found
from pysaas.pages.terms import terms
from pysaas.pages.privacy import privacy
from pysaas.pages.cookies import cookies
from pysaas.styles import BASE_STYLE

# Configure secrets
load_dotenv()

LM_API_KEY = os.environ.get("LM_API_KEY")
LM_SIGNING_SECRET = os.environ.get("LM_SIGNING_SECRET")
LM_URL = os.environ.get("LM_URL")

NOTION_API_KEY = os.environ.get("NOTION_API_KEY")
NOTION_DB_ID = os.environ.get("NOTION_DB_ID")

firebase_config = {
    "apiKey": os.environ.get("FIREBASE_API_KEY"),
    "authDomain": os.environ.get("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.environ.get("FIREBASE_DB_URL"),
    "projectId": os.environ.get("FIREBASE_PROJECT_ID"),
    "storageBucket": os.environ.get("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.environ.get("FIREBASE_MSG_SENDER_ID"),
    "appId": os.environ.get("FIREBASE_APP_ID"),
    "measurementId": os.environ.get("FIREBASE_MEASUREMENT_ID"),
}
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()

btc = yf.Ticker("BTC-USD")
btc = pd.DataFrame(btc.history(period="1mo", rounding="True"))
btc.reset_index(inplace=True)
btc["Date"] = btc["Date"].dt.strftime('%Y/%m/%d')
btc = btc[["Date", "Open", "High", "Low", "Close", "Volume"]]


# The main app state class
# Other state classes inherit from State
class State(rx.State):
    user_email: Optional[str] = None
    name: Optional[str] = None
    plan: bool = False
    renews_at: Optional[str] = None
    sub_id: Optional[str] = None
    manage_sub_url: Optional[str] = None
    id_token: Optional[str] = None
    refresh_token: Optional[str] = None
    signed_in: bool = False
    show_spinner: bool = True
    sent_reset_email: bool = False

    @rx.var
    def signed_out(self):
        return not self.signed_in

    @rx.var
    def get_user_email(self) -> str:
        if self.user_email is None:
            return ""
        return self.user_email.lower()

    @rx.var
    def get_user_name(self) -> str:
        if self.name is None:
            return ""
        return self.name

    @rx.var
    def get_renew_date(self) -> str:
        if not self.renews_at:
            return ""
        return parser.isoparse(self.renews_at).strftime("%B %d, %Y")

    @rx.var
    def get_manage_sub_url(self) -> str:
        if not self.manage_sub_url:
            return ""
        return self.manage_sub_url

    @rx.var
    def get_lm_url(self) -> str:
        if self.signed_in:
            return LM_URL + "?checkout[email]=" + self.user_email
        return LM_URL


# The auth state class
# Handles user authentication status and flow
class AuthState(State):
    email_field: str = ""
    password_field: str = ""
    confirm_password_field: str = ""
    error_message: str = ""
    show_error: bool = False

    def set_email(self, email):
        self.email_field = email

    def set_password(self, password):
        self.password_field = password

    def set_confirm_password(self, password):
        self.confirm_password_field = password

    def clear_errors(self):
        self.error_message = ""
        self.show_error = False

    def verify_and_load(self):
        if self.signed_out:
            return rx.redirect("/signin")

        DashState.load_data("BTC")

        try:
            users = db.child("users").get().each()
            for user in users:
                if user.val()["email"] == self.user_email:
                    self.plan = user.val()["plan"]
                    self.renews_at = user.val()["renews_at"]
                    self.sub_id = user.val()["sub_id"]

                    if self.sub_id:
                        try:
                            url = f"https://api.lemonsqueezy.com/v1/subscriptions/{self.sub_id}"
                            r = requests.get(url, headers={
                                "Authorization": f"Bearer {LM_API_KEY}",
                                "Accept": "application/vnd.api+json",
                                "Content-Type": "application/vnd.api+json"
                            })
                            result_dict = json.loads(r.text)
                            data = result_dict["data"]
                            self.manage_sub_url = data["attributes"]["urls"]["update_payment_method"]
                        except:
                            self.manage_sub_url = ""
                    else:
                        self.manage_sub_url = ""
        except:
            self.plan = False
            self.renews_at = ""
            self.sub_id = ""
            self.manage_sub_url = ""

    def signin(self):
        try:
            user = auth.sign_in_with_email_and_password(self.email_field, self.password_field)
            if user["registered"]:
                self.user_email = user["email"]
                self.id_token = user["idToken"]
                self.refresh_token = user["refreshToken"]

                users = db.child("users").get().each()
                for user in users:
                    if user.val()["email"] == self.user_email:
                        self.name = user.val()["name"]
                        self.plan = user.val()["plan"]
                        self.renews_at = user.val()["renews_at"]
                        self.sub_id = user.val()["sub_id"]
                        self.signed_in = True
                        DashState.name_field = self.name
                        return rx.redirect("/dashboard")

            self.error_message = "Invalid email or password. Try again."
            self.show_error = True
            return
        except:
            self.error_message = "Invalid email or password. Try again."
            self.show_error = True
            return

    def signup(self):
        try:
            validation = validate_email(self.email_field, check_deliverability=True)
            self.email_field = validation.email
        except Exception as e:
            self.error_message = str(e)
            self.show_error = True
            return

        if len(self.password_field) < 6:
            self.error_message = "Password must contain at least 6 characters."
            self.show_error = True
            return

        if self.password_field != self.confirm_password_field:
            self.error_message = "Passwords do not match."
            self.show_error = True
            return

        try:
            new_user = auth.create_user_with_email_and_password(self.email_field, self.password_field)
            self.user_email = new_user["email"]
            self.name = ""
            self.plan = False
            self.renews_at = ""
            self.sub_id = ""
            self.manage_sub_url = ""
            self.id_token = new_user["idToken"]
            self.refresh_token = new_user["refreshToken"]

            user_data = {
                "email": self.user_email,
                "name": self.name,
                "plan": self.plan,
                "renews_at": self.renews_at,
                "sub_id": self.sub_id
            }
            db.child("users").push(user_data)

            self.signed_in = True
            DashState.name_field = self.name
            return rx.redirect("/dashboard")
        except:
            self.error_message = "Email already exists."
            self.show_error = True
            return

    def signout(self):
        self.user_email = None
        self.name = None
        self.plan = False
        self.renews_at = None
        self.sub_id = None
        self.manage_sub_url = None
        self.id_token = None
        self.refresh_token = None
        self.signed_in = False
        return rx.redirect("/")


# The index state class
# Define pricing options to display
class IndexState(State):
    yearly_pricing: bool = False
    pro_mo: str = "$9"
    pro_yr: str = "$90"
    premium_mo: str = "$69"
    premium_yr: str = "$690"
    enterprise_mo: str = "$420"
    enterprise_yr: str = "$4200"

    def toggle_pricing(self, checked):
        self.yearly_pricing = checked


# The blog list state class
# Retrieves a list of active posts from your Notion database to display on the /blog route
class BlogState(State):
    posts: list[Post] = []

    def load_posts(self):
        url = f"https://api.notion.com/v1/databases/{NOTION_DB_ID}/query"
        r = requests.post(url, headers={
            "Authorization": f"Bearer {NOTION_API_KEY}",
            "Notion-Version": "2022-06-28"
        })
        result_dict = r.json()
        results = result_dict["results"]

        self.posts = []
        for result in results:
            date = result["properties"]["published"]["date"]["start"]
            title = result["properties"]["name"]["title"][0]["text"]["content"]
            subtitle = result["properties"]["subtitle"]["rich_text"][0]["text"]["content"]
            tags = result["properties"]["tags"]["multi_select"]
            thumbnail_url = result["properties"]["thumbnail"]["files"][0]["file"]["url"]
            slug = result["properties"]["slug"]["rich_text"][0]["text"]["content"]
            active = result["properties"]["active"]["checkbox"]

            hashtags = ""
            for tag in tags:
                hashtags += ("#" + tag["name"] + " ")
            hashtags = hashtags[:-1]

            if active:
                self.posts.append(Post(date, title, subtitle, hashtags, thumbnail_url, slug))

        self.posts.sort(key=lambda post: post.date, reverse=True)
        self.show_spinner = False


# The blog post state class
# Retrieves contents of a particular post from your Notion database on the /blog/<slug> route
class PostState(State):
    paragraphs: list[list[PostSectionContent]] = []
    content: list[PostSectionContent] = []
    page_id: str = ""
    date: str = ""
    title: str = ""
    subtitle: str = ""
    current_text: str = ""

    @rx.var
    def post_slug(self):
        return self.get_query_params().get("slug", "No slug")

    def load_post(self):
        url = f"https://api.notion.com/v1/databases/{NOTION_DB_ID}/query"
        r = requests.post(url, headers={
            "Authorization": f"Bearer {NOTION_API_KEY}",
            "Notion-Version": "2022-06-28"
        })
        result_dict = r.json()
        results = result_dict["results"]

        self.paragraphs = []
        self.content = []
        self.page_id = ""
        for result in results:
            slug = result["properties"]["slug"]["rich_text"][0]["text"]["content"]
            active = result["properties"]["active"]["checkbox"]
            if slug == self.post_slug and active:
                self.date = result["properties"]["published"]["date"]["start"]
                self.title = result["properties"]["name"]["title"][0]["text"]["content"]
                self.subtitle = result["properties"]["subtitle"]["rich_text"][0]["text"]["content"]
                self.page_id = result["id"]

        if not self.page_id:
            return rx.redirect("/oops")

        url = f"https://api.notion.com/v1/blocks/{self.page_id}/children?page_size=100"
        r = requests.get(url, headers={
            "Authorization": f"Bearer {NOTION_API_KEY}",
            "Notion-Version": "2022-06-28"
        })
        result_dict = r.json()
        results = result_dict["results"]
        from pprint import pprint
        pprint(results)

        for result in results:
            # PARAGRAPH DETECTION
            if result["type"] == "paragraph":
                full_content = result["paragraph"]["rich_text"]
                running_html = ''
                for part in full_content:
                    if part["type"] == "text":
                        if not part["text"]["link"]:
                            # check for edge case of only punctuation at the end, slice the space off before it
                            if part['text']['content'] in ['.', '?', '!', ',', ':', ';']:
                                running_html = running_html[:-1]
                            if part['annotations']['italic']:
                                running_html += f'<em>{part["text"]["content"]}</em> '
                            elif part['annotations']['underline']:
                                running_html += f'<u>{part["text"]["content"]}</u> '
                            elif part['annotations']['bold']:
                                running_html += f'<b>{part["text"]["content"]}</b> '
                            else:
                                running_html += f'{part["text"]["content"]} '
                        else:
                            # don't include space after in the link, append space after link
                            running_html += f'<a href="{part["text"]["link"]["url"]}" target="_blank">{part["text"]["content"]}</a>' + ' '
                self.content.append(PostSectionContent(is_text=True, html=running_html))
            # HEADINGS DETECTION
            elif 'heading' in result['type']:
                running_content = PostSectionContent(is_heading=True)
                if result['type'] == 'heading_1':
                    running_content.is_h1 = True
                    running_content.content = result['heading_1']['rich_text'][0]['plain_text']
                elif result['type'] == 'heading_2':
                    running_content.is_h2 = True
                    running_content.content = result['heading_2']['rich_text'][0]['plain_text']
                elif result['type'] == 'heading_3':
                    running_content.is_h3 = True
                    running_content.content = result['heading_3']['rich_text'][0]['plain_text']
                elif result['type'] == 'heading_4':
                    running_content.is_h4 = True
                    running_content.content = result['heading_4']['rich_text'][0]['plain_text']
                self.content.append(running_content)
            # BULLETED LIST DETECTION
            elif result['type'] == 'bulleted_list_item':
                list_item = f"<li>{result['bulleted_list_item']['rich_text'][0]['plain_text']}</li>"
                self.content.append(PostSectionContent(is_ul=True, html=list_item))
            elif result['type'] == 'numbered_list_item':
                list_item = f"<li>{result['numbered_list_item']['rich_text'][0]['plain_text']}</li>"
                self.content.append(PostSectionContent(is_ol=True, html=list_item))
            # EMBED DETECTION - supports Twitter, doesn't render fully all the time (yet)
            elif result['type'] == 'embed':
                if 'twitter' in result['embed']['url']:
                    url = result['embed']['url']
                    get_tweet_url = f'https://publish.twitter.com/oembed?url={url}&hide_media=true&hide_thread=true&align=center&omit_script=true'
                    r = requests.get(get_tweet_url)
                    result_dict = r.json()
                    html = result_dict['html']
                    self.content.append(PostSectionContent(is_link=True, is_embed=True, url=url, html=html))
            elif result["type"] == "image":
                if result["image"]["type"] == "file":
                    self.content.append(PostSectionContent(is_image=True, url=result["image"]["file"]["url"]))
            self.paragraphs.append(self.content)
            self.content = []

        self.show_spinner = False


# The dashboard state class
# Your app's logic goes here
# Details:
#   1. The /dashboard route is viewable only to authenticated users
#   2. This is an example application that displays cryptocurrency price data from the past month
#   3. Users can only view the full selection of data by subscribing to a paid plan
#   4. You can use this code as a reference in developing your application's logic
class DashState(State):
    # State variables for example dashboard app data
    data: pd.DataFrame = btc
    close: list[int] = list(btc["Close"])

    # State variables for user management
    name_field: str = ""
    password_field: str = ""
    email_error_message: str = ""
    profile_error_message: str = ""
    cancel_error_message: str = ""
    show_email_error: bool = False
    show_profile_error: bool = False
    show_cancel_error: bool = False
    alert_message: str = ""
    alert_heading: str = ""
    close_button_message: str = ""
    show_alert: bool = False
    confirmed_cancel: bool = False

    # State functions for example dashboard app data
    @rx.var
    def data_len(self) -> int:
        return len(self.close)

    @rx.var
    def curr_price(self) -> str:
        return "$" + str(self.close[len(self.close) - 1])

    @rx.var
    def delta(self) -> str:
        return str(round(100 * (self.close[len(self.close) - 1] - self.close[0]) / self.close[0], 2))

    @rx.var
    def increase(self) -> bool:
        return (self.close[len(self.close) - 1] - self.close[0]) / self.close[0] > 0

    def load_data(self, coin):
        data = yf.Ticker(coin + "-USD")
        data = pd.DataFrame(data.history(period="1mo", rounding="True"))
        data.reset_index(inplace=True)
        data['Date'] = data['Date'].dt.strftime('%Y/%m/%d')

        self.data = data[["Date", "Open", "High", "Low", "Close", "Volume"]]
        self.close = list(self.data["Close"])

    # State functions for user management
    def set_name(self, name):
        self.name_field = name

    def set_password(self, password):
        self.password_field = password

    def toggle_alert(self):
        self.show_alert = not self.show_alert

    def toggle_checked(self, checked):
        self.confirmed_cancel = checked

    def cancel_subscription(self):
        if not self.confirmed_cancel:
            return

        if self.sub_id:
            try:
                url = f"https://api.lemonsqueezy.com/v1/subscriptions/{self.sub_id}"
                r = requests.delete(url, headers={
                    "Authorization": f"Bearer {LM_API_KEY}",
                    "Accept": "application/vnd.api+json",
                    "Content-Type": "application/vnd.api+json"
                })
                result_dict = json.loads(r.text)
                data = result_dict["data"]
                if data["attributes"]["status"] == "cancelled":
                    users = db.child("users").get().each()
                    for user in users:
                        if user.val()["email"] == self.user_email:
                            self.plan = False
                            self.renews_at = ""
                            self.sub_id = ""
                            db.child("users").child(user.key()).update({"plan": self.plan})
                            db.child("users").child(user.key()).update({"renews_at": self.renews_at})
                            db.child("users").child(user.key()).update({"sub_id": self.sub_id})
                            return rx.redirect("/dashboard")

                self.cancel_error_message = "Failed to cancel subscription. Try again."
                self.show_cancel_error = True
            except:
                self.cancel_error_message = "Failed to cancel subscription. Try again."
                self.show_cancel_error = True

    def update_user_data(self):
        if self.signed_out:
            return rx.redirect("/signin")

        try:
            users = db.child("users").get().each()
            for user in users:
                if user.val()["email"] == self.user_email:
                    db.child("users").child(user.key()).update({"name": self.name_field})
                    self.name = self.name_field
                    self.show_profile_error = False
                    self.alert_message = "Updated account profile information."
                    self.alert_heading = "Success!"
                    self.close_button_message = "Close"
                    self.show_alert = True
                    return

            self.profile_error_message = "Failed to update user data. Try again."
            self.show_profile_error = True
            return
        except:
            self.profile_error_message = "Failed to update user data. Try again."
            self.show_profile_error = True
            return

    def send_password_reset(self):
        if self.signed_out:
            return rx.redirect("/signin")

        try:
            user = auth.sign_in_with_email_and_password(self.user_email, self.password_field)
            if user["registered"]:
                try:
                    auth.send_password_reset_email(self.user_email)
                    self.show_email_error = False
                    self.alert_message = "Sent password reset email to " + self.user_email
                    self.alert_heading = "Success!"
                    self.close_button_message = "Close"
                    self.show_alert = True
                    return
                except:
                    self.email_error_message = "Failed to send email. Try again."
                    self.show_email_error = True
                    return

            self.email_error_message = "Failed to send email. Try again."
            self.show_email_error = True
            return
        except:
            self.email_error_message = "Password is invalid. Try again."
            self.show_email_error = True
            return


# Configure app with main state class
app = rx.App(state=State, style=BASE_STYLE)


@app.api.get("/health-check", status_code=200)
async def health_check():
    return {"status": "healthy"}


# Webhook listener
# Allows your app to stay in sync with Lemon Squeezy subscription updates
@app.api.post("/webhooks/lmsqueezy", status_code=200)
async def subscription_update(request: Request):
    payload = await request.body()
    signature = request.headers.get("X-Signature")
    digest = hmac.new(LM_SIGNING_SECRET.encode(), payload, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(digest, signature):
        raise Exception(400, "Invalid signature.")

    body = json.loads(payload)
    try:
        event = body["meta"]["event_name"]
        if event == "subscription_created" or event == "subscription_updated":
            sub_id = body["data"]["id"]
            user_email = body["data"]["attributes"]["user_email"]
            status = body["data"]["attributes"]["status"]
            if status == "active":
                renews_at = body["data"]["attributes"]["renews_at"]
                users = db.child("users").get().each()
                for user in users:
                    if user.val()["email"] == user_email:
                        db.child("users").child(user.key()).update({"sub_id": sub_id})
                        db.child("users").child(user.key()).update({"plan": True})
                        db.child("users").child(user.key()).update({"renews_at": renews_at})
                        return {"message": f"Saved active plan details for {user_email}"}
            elif status == "unpaid" or status == "cancelled" or status == "expired":
                users = db.child("users").get().each()
                for user in users:
                    if user.val()["email"] == user_email:
                        db.child("users").child(user.key()).update({"sub_id": ""})
                        db.child("users").child(user.key()).update({"plan": False})
                        db.child("users").child(user.key()).update({"renews_at": ""})
                        return {"message": f"Saved inactive plan details for {user_email}"}
        return {"message": "No updates made"}
    except Exception as e:
        raise HTTPException(400, detail=str(e))


# Define app pages and routes
app.add_page(
    index,
    title="PySaaS",
    description="TBD description.",
    image="/preview.png",
)
app.add_page(
    blog,
    title="PySaaS | Blog",
    description="TBD description.",
    image="/preview.png",
    on_load=BlogState.load_posts,
)
app.add_page(
    post,
    title="PySaaS | Blog",
    description="TBD description.",
    image="/preview.png",
    route="/blog/[slug]",
    on_load=PostState.load_post,
)
# app.add_page(
#     signin,
#     title="PySaaS | Sign in",
#     description="TBD description.",
#     image="/preview.png",
#     on_load=AuthState.clear_errors,
# )
# app.add_page(
#     signup,
#     title="PySaaS | Sign up",
#     description="TBD description.",
#     image="/preview.png",
#     on_load=AuthState.clear_errors,
# )
# app.add_page(
#     signout,
#     title="PySaaS | Sign out",
#     description="TBD description.",
#     image="/preview.png",
#     on_load=AuthState.signout,
# )
# app.add_page(
#     dashboard,
#     title="PySaaS | Dashboard",
#     description="TBD description.",
#     image="/preview.png",
#     on_load=AuthState.verify_and_load,
# )
app.add_custom_404_page(
    not_found,
    title="PySaaS | Page not found",
    description="TBD description.",
    image="/preview.png",
)
app.add_page(
    terms,
    title='PySaaS | Terms and Condition',
    description='TBD description',
    image='/preview.png',
)
app.add_page(
    privacy,
    title='PySaaS | Privacy Policy',
    description='TBD Description',
    image='/preview.png',
)
app.add_page(
    cookies,
    title='PySaaS | Cookies Policy',
    description='TBD description',
    image='/preview.png',
)

app.compile()
