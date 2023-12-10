import reflex as rx

from pysaas import styles
from pysaas import pysaas


class Post(rx.Model, table=True):
    date: str
    title: str 
    subtitle: str
    tags: str
    thumbnail_url: str
    slug: str

    def __init__(self, date, title, subtitle, tags, thumbnail_url, slug):
        self.date = date
        self.title = title
        self.subtitle = subtitle
        self.tags = tags
        self.thumbnail_url = thumbnail_url
        self.slug = slug


class PostSectionContent(rx.Model, table=True):
    is_heading: bool = False
    is_h1: bool = False
    is_h2: bool = False
    is_h3: bool = False
    is_h4: bool = False
    is_link: bool = False
    is_image: bool = False
    is_text: bool = False
    is_embed: bool = False
    is_ul: bool = False
    is_ol: bool = False
    content: str = ""
    url: str = ""
    html: str = ''


def posts() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.tablet_and_desktop(
                    rx.text(
                        "Blog",
                        font_size="2em",
                        font_weight=700,
                    ),
                    text_align="center",
                    line_height="1.15",
                    padding_bottom="0.5em",
                ),
                rx.mobile_only(
                    rx.text(
                        "Blog",
                        font_size="1.5em",
                        font_weight=700,
                    ),
                    text_align="center",
                    line_height="1.15",
                    padding_bottom="0.5em",
                ),
                rx.tablet_and_desktop(
                    rx.container(
                        "Welcome to your new blog page, built in pure Python.",
                        color="grey",
                        font_size="1.25em",
                        text_align="center",
                        padding_bottom="3em"
                    ),
                ),
                rx.mobile_only(
                    rx.container(
                        "Welcome to your new blog page, built in pure Python.",
                        color="grey",
                        font_size="1.25em",
                        text_align="center",
                        padding_bottom="1.5em"
                    ),
                ),
                rx.cond(
                    pysaas.State.show_spinner,
                    rx.center(
                        rx.spinner(
                            color="black",
                            thickness=5,
                            speed="1.25s",
                            size="xl",
                        ),
                    ),
                ),
                rx.box(
                    rx.foreach(pysaas.BlogState.posts, post_preview),
                    padding_right="3em",
                ),
            ),
        ),
        width="100%",
        padding_top="5%",
    )


def post_preview(post: Post) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.tablet_and_desktop(
                rx.box(
                    rx.vstack(
                        rx.link(
                            rx.image(
                                src=post.thumbnail_url,
                                width="100%",
                                border_radius="15px",
                            ),
                            href="/blog/" + post.slug,
                            margin_bottom="1em",
                            min_height="12em",
                            width="25em",
                            padding_left="3em",
                        ),
                        width="25em",
                    ),
                ),
            ),
            rx.box(
                rx.vstack(
                    rx.link(
                        rx.text(
                            post.title,
                            font_size=styles.H2_FONT_SIZE,
                            font_weight=styles.BOLD_WEIGHT,
                        ),
                        href="/blog/" + post.slug,
                        _hover={
                            "color": styles.ACCENT_COLOR,
                        },
                    ),
                    rx.text(
                        post.subtitle,
                        color="#676767",
                    ),
                    rx.text(
                        post.date + " ",
                        rx.span(
                            post.tags,
                            font_weight="bold",
                        ),
                        color="#676767",
                    ),
                    rx.link(
                        rx.button(
                            "Read More",
                            bg="white",
                            box_shadow=styles.DOC_SHADOW_LIGHT,
                            color="black",
                            margin_top=0,
                            size="sm",
                            border="2px solid black",
                            _hover={
                                "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                            },
                            width="100px",
                        ),
                        href="/blog/" + post.slug,
                        _hover={
                            "text_decoration": "none",
                        },
                    ),
                    margin_bottom="1em",
                    min_height="12em",
                    align_items="left",
                ),
            ),
            spacing="3em",
            padding_top="2em",
        ),
        padding_top="1em",
        align_items="left",
    )


def post_paragraph(paragraph: list[PostSectionContent]) -> rx.Component:
    return rx.box(
        rx.foreach(paragraph, post_content),
        padding_y="0.5em",
    )


def post_content(post_content: PostSectionContent) -> rx.Component:
    """Takes each post section and returns the proper rx.component to render

    Args:
        post_content (PostSectionContent): Post Section Content to render

    Returns:
        rx.Component: Appropriate component for section
    """
    return rx.span(
        # check for header
        rx.cond(
            post_content.is_heading,
            rx.cond(
                post_content.is_h1,
                rx.text(
                    post_content.content,
                    font_size=styles.H1_FONT_SIZE,
                    font_weight=styles.BOLD_WEIGHT,
                    style=styles.HEADING_COLOR_GRADIENT,
                ),
                rx.cond(
                    post_content.is_h2,
                    rx.text(
                        post_content.content,
                        font_size=styles.H2_FONT_SIZE,
                        font_weight=styles.BOLD_WEIGHT,
                        style=styles.HEADING_COLOR_GRADIENT,
                    ),
                    rx.cond(
                        post_content.is_h3,
                        rx.text(
                            post_content.content,
                            font_size=styles.H3_FONT_SIZE,
                            font_weight=styles.BOLD_WEIGHT,
                        ),
                        rx.cond(
                            post_content.is_h4,
                            rx.text(
                                post_content.content,
                                font_size=styles.H4_FONT_SIZE,
                                font_weight=styles.BOLD_WEIGHT,
                            ),
                        ),
                    ),
                ),
            ),
            # check for image
            rx.cond(
                post_content.is_image,
                rx.box(
                    rx.center(
                        rx.image(
                            src=post_content.url,
                            width="100%",
                            border_radius="5em",
                            padding_y="2em",
                        ),
                    ),
                ),
                # check for embed
                rx.cond(
                    post_content.is_embed,
                    rx.fragment(
                        rx.script("""window.twttr = (function(d, s, id) { var js, fjs = d.getElementsByTagName(s)[0], t = window.twttr || {}; if (d.getElementById(id)) return t; js = d.createElement(s); js.id = id; js.src = "https://platform.twitter.com/widgets.js"; fjs.parentNode.insertBefore(js, fjs); t._e = []; t.ready = function(f) { t._e.push(f); }; return t; }(document, "script", "twitter-wjs"));"""),
                        rx.html(post_content.html),
                    ),
                    # check for text
                    rx.cond(
                        post_content.is_text,
                        rx.html(post_content.html),
                        # check for bullet list
                        rx.cond(
                            post_content.is_ul,
                            rx.html(post_content.html),
                            # check for ordered list
                            rx.cond(
                                post_content.is_ol,
                                rx.html(post_content.html)
                            )
                        ),
                    )
                )
            )
        )
    )


def post_details() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.tablet_and_desktop(
                    rx.text(
                        pysaas.PostState.title,
                        font_size="2em",
                        font_weight=700,
                    ),
                    text_align="center",
                    line_height="1.15",
                    padding_bottom="0.5em",
                ),
                rx.mobile_only(
                    rx.text(
                        pysaas.PostState.title,
                        font_size="1.5em",
                        font_weight=700,
                    ),
                    text_align="center",
                    line_height="1.15",
                    padding_bottom="0.4em",
                ),
                rx.tablet_and_desktop(
                    rx.container(
                        pysaas.PostState.subtitle,
                        color="grey",
                        font_size="1.25em",
                        text_align="center",
                        padding_bottom="0.5em",
                    ),
                ),
                rx.mobile_only(
                    rx.container(
                        pysaas.PostState.subtitle,
                        color="grey",
                        font_size="1.25em",
                        text_align="center",
                        padding_bottom="0.4em",
                    ),
                ),
                rx.tablet_and_desktop(
                    rx.center(
                        rx.hstack(
                            rx.cond(
                                ~pysaas.State.show_spinner,
                                rx.icon(tag="calendar"),
                            ),
                            rx.span(" " + pysaas.PostState.date),
                            color="black",
                            font_size="1.1em",
                            font_weight="435",
                            text_align="center",
                            padding_bottom="1.5em",
                        ),
                    ),
                ),
                rx.mobile_only(
                    rx.center(
                        rx.hstack(
                            rx.cond(
                                ~pysaas.State.show_spinner,
                                rx.icon(tag="calendar"),
                            ),
                            rx.span(" " + pysaas.PostState.date),
                            color="black",
                            font_size="0.95em",
                            font_weight="435",
                            text_align="center",
                            padding_bottom="1.1em",
                        ),
                    ),
                ),
                rx.tablet_and_desktop(
                    rx.cond(
                        ~pysaas.State.show_spinner,
                        rx.html("<hr>"),
                    ),
                    padding_bottom="1.5em",
                ),
                rx.mobile_only(
                    rx.cond(
                        ~pysaas.State.show_spinner,
                        rx.html("<hr>"),
                    ),
                    padding_bottom="1.1em",
                ),
                rx.cond(
                    pysaas.State.show_spinner,
                    rx.center(
                        rx.spinner(
                            color="black",
                            thickness=5,
                            speed="1.25s",
                            size="xl",
                        ),
                    ),
                ),
                rx.box(
                    rx.foreach(pysaas.PostState.paragraphs, post_paragraph),
                ),
                rx.cond(
                    ~pysaas.State.show_spinner,
                    rx.box(
                        rx.vstack(
                            rx.image(
                                src="/logo.svg",
                                height="2em",
                                width="2em",
                            ),
                            rx.text(
                                "Start your free trial today.",
                                font_size=styles.H3_FONT_SIZE,
                                font_weight=styles.BOLD_WEIGHT,
                                color="black",
                            ),
                            rx.text(
                                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation. ",
                                rx.cond(
                                    pysaas.State.signed_out,
                                    rx.span(
                                        rx.link(
                                            "Get started →",
                                            href="/signup",
                                            color=styles.ACCENT_COLOR,
                                        ),
                                    ),
                                    rx.span(
                                        rx.link(
                                            "Get started →",
                                            href="/dashboard",
                                            color=styles.ACCENT_COLOR,
                                        ),
                                    ),
                                ),
                                color="#676767",
                            ),
                            margin_bottom="1em",
                            style=styles.BOX_STYLES,
                            min_height="12em",
                        ),
                        padding_top="3em",
                    ),
                ),
                width="60%",
            ),
        ),
        width="100%",
        padding_top="5%",
    )