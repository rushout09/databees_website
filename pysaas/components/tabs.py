import reflex as rx

from pysaas import styles
from pysaas import pysaas
from pysaas.components.landing import purchase_cards


def data_table() -> rx.Component:
    return rx.box(
        rx.data_table(
            data=pysaas.DashState.data,
            pagination=True,
            search=True,
            sort=True,
        ),
    )


def dash_heading() -> rx.Component:
    return rx.box(
        rx.heading(
            "Dashboard",
            font_weight="500",
            font_size="1.75em",
        ),
        rx.text(
            "Your app goes here. This is an example dashboard.",
            font_weight="349",
            padding_top="0.3em",
            padding_bottom="0.5em",
        ),
        rx.cond(
            ~pysaas.State.plan,
            rx.box(
                rx.box(
                    rx.vstack(
                        rx.box(
                            rx.box(
                                rx.text(
                                    rx.span(
                                        "Note: ",
                                        font_weight="600",
                                    ),
                                    "You're on a free plan. Upgrade your subscription to access OHLCV trade data for more crypto assets.",
                                    font_weight="350",
                                ),
                            ),
                            rx.box(
                                rx.link(
                                    rx.button(
                                        "Upgrade Subscription",
                                        bg="black",
                                        box_shadow=styles.DOC_SHADOW_LIGHT,
                                        color="white",
                                        margin_top=0,
                                        size="sm",
                                        border="2px solid black",
                                        _hover={
                                            "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                                        },
                                        width="100%",
                                    ),
                                    href=pysaas.State.get_lm_url,
                                ),
                                width="12em",
                                padding_y="0.2em",
                            ),
                        ),
                        align_items="left",
                    ),
                    width="100%",
                    style=styles.DASH_STYLES,
                ),
                padding_top="0.85em",
            ),
        ),
    )


def selector() -> rx.Component:
    return rx.hstack(
        rx.cond(
            ~pysaas.State.plan,
            rx.box(
                rx.select(
                    ["BTC", "ETH", "LINK"],
                    is_disabled=True,
                ),
                width="15em",
            ),
            rx.box(
                rx.select(
                    ["BTC", "ETH", "LINK"],
                    is_disabled=False,
                    on_change=pysaas.DashState.load_data,
                ),
                width="15em",
            ),
        ),
        rx.stat_group(
            rx.cond(
                pysaas.DashState.increase,
                rx.stat(
                    rx.stat_number(pysaas.DashState.curr_price),
                    rx.stat_help_text(
                        pysaas.DashState.delta + "% ", 
                        rx.stat_arrow(type_="increase")
                    ),
                ),
                rx.stat(
                    rx.stat_number(pysaas.DashState.curr_price),
                    rx.stat_help_text(
                        pysaas.DashState.delta + "% ", 
                        rx.stat_arrow(type_="decrease")
                    ),
                ),
            ),
            width="100%",
            padding_top="0.85em",
        ),
        spacing="1em",
    )


def sub_heading() -> rx.Component:
    return rx.box(
        rx.heading(
            "Subscription",
            font_weight="500",
            font_size="1.75em",
        ),
        rx.text(
            "Manage your subscription plan",
            font_weight="349",
            padding_top="0.3em",
            padding_bottom="1.5em",
        ),
    )


def sub_management() -> rx.Component:
    return rx.box(
        rx.cond(
            ~pysaas.State.plan,
            purchase_cards(),
            rx.box(
                rx.vstack(
                    rx.heading(
                        "Pro ",
                        rx.span(
                            rx.badge(
                                "Active", variant="subtle", color_scheme="green"
                            ),
                            padding_left="0.15em",
                        ),
                        font_weight="550",
                        font_size="1.5em",
                    ),
                    rx.text(
                        "Description of your subscription plan",
                        font_weight="349",
                        font_size="1.1em",
                        padding_bottom="0.5em",
                    ),
                    rx.text(
                        rx.span(
                            pysaas.IndexState.pro_mo,
                            font_size=styles.H2_FONT_SIZE,
                            font_weight=styles.BOLD_WEIGHT,
                            color="black",
                        ),
                        " / month",
                        font_size=styles.H4_FONT_SIZE,
                    ),
                    rx.text(
                        rx.span(
                            rx.icon(tag="check_circle", color="black"),
                        ),
                        " Your subscription is scheduled to be renewed on " + pysaas.State.get_renew_date,
                        font_weight="349",
                        font_size="0.9em",
                        padding_bottom="1em",
                    ),
                    rx.box(
                        rx.link(
                            rx.button(
                                "Update Payment Method",
                                bg="black",
                                box_shadow=styles.DOC_SHADOW_LIGHT,
                                color="white",
                                margin_top=0,
                                size="sm",
                                border="2px solid black",
                                _hover={
                                    "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                                },
                                width="100%",
                            ),
                            href=pysaas.State.get_manage_sub_url,
                            _hover={"text_decoration": "none"},
                        ),
                        width="14em",
                        padding_bottom="2.5em",
                    ),
                    rx.heading(
                        "Cancel Subscription",
                        font_weight="500",
                        font_size="1.05em",
                    ),
                    rx.form_control(
                        rx.form_label(
                            "Are you sure?",
                            font_weight="420",
                        ),
                        rx.checkbox("Confirm", on_change=pysaas.DashState.toggle_checked),
                        rx.form_helper_text(
                            "If you cancel this plan, it will no longer be available to you.",
                            color="grey",
                            font_size="0.8em",
                        ),
                        is_required=True,
                        padding_bottom="0.25em",
                    ),
                    rx.box(
                        rx.cond(
                            pysaas.DashState.show_cancel_error,
                            rx.wrap(
                                rx.text(
                                    pysaas.DashState.cancel_error_message,
                                    font_size="0.8em",
                                    color="#DC143C",
                                    font_weight="330",
                                    padding_bottom="0.25em",
                                ),
                            ),
                        ),
                    ),
                    rx.box(
                        rx.button(
                            "Cancel Subscription",
                            on_click=pysaas.DashState.cancel_subscription,
                            bg="black",
                            box_shadow=styles.DOC_SHADOW_LIGHT,
                            color="white",
                            margin_top=0,
                            size="sm",
                            border="2px solid black",
                            _hover={
                                "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                            },
                            width="16em",
                        ),
                        padding_bottom="0.1em",
                    ),
                    rx.text(
                        "By canceling your plan, you agree to the Terms of Service and Privacy Policy.",
                        color="grey",
                        font_size="0.8em",
                        font_weight="350",
                        padding_bottom="1.25em",
                    ),
                    align_items="left",
                ),
            ),
        ),
        padding_x="1.5em",
        padding_y="1.5em",
        style=styles.DASH_STYLES,
    )


def account_profile() -> rx.Component:
    return rx.box(
        rx.heading(
            "Account Profile",
            font_weight="500",
            font_size="1.2em",
            padding_bottom="1em",
        ),
        rx.avatar(size="md"),
        rx.box(
            rx.text(
                "Name",
                font_size="0.85em",
                padding_bottom="0.1em",
                color="#676767",
            ),
            rx.input(
                placeholder="Name",
                default_value=pysaas.State.get_user_name,
                on_blur=pysaas.DashState.set_name,
                color="black",
                type="email",
                size="md",
                border="2px solid #f4f4f4",
                box_shadow="rgba(0, 0, 0, 0.08) 0px 4px 12px",
                bg="rgba(255,255,255,.5)",
                _focus={
                    "border": f"2px solid {styles.ACCENT_COLOR}",
                },
            ),
            width="14em",
            padding_top="1em",
        ),
        rx.box(
            rx.text(
                "Email Address",
                font_size="0.85em",
                padding_bottom="0.1em",
                color="#676767",
            ),
            rx.input(
                value=pysaas.State.get_user_email,
                is_disabled=True,
                color="black",
                type="email",
                size="md",
                border="2px solid #f4f4f4",
                box_shadow="rgba(0, 0, 0, 0.08) 0px 4px 12px",
                bg="rgba(255,255,255,.5)",
                _focus={
                    "border": f"2px solid {styles.ACCENT_COLOR}",
                },
            ),
            width="14em",
            padding_top="0.5em",
        ),
        rx.box(
            rx.text(
                "Subscription Plan",
                font_size="0.85em",
                padding_bottom="0.1em",
                color="#676767",
            ),
            rx.cond(
                ~pysaas.State.plan,
                rx.input(
                    value="Free Plan",
                    is_disabled=True,
                    color="black",
                    size="md",
                    border="2px solid #f4f4f4",
                    box_shadow="rgba(0, 0, 0, 0.08) 0px 4px 12px",
                    bg="rgba(255,255,255,.5)",
                    _focus={
                        "border": f"2px solid {styles.ACCENT_COLOR}",
                    },
                ),
                rx.input(
                    value="Pro",
                    is_disabled=True,
                    color="black",
                    size="md",
                    border="2px solid #f4f4f4",
                    box_shadow="rgba(0, 0, 0, 0.08) 0px 4px 12px",
                    bg="rgba(255,255,255,.5)",
                    _focus={
                        "border": f"2px solid {styles.ACCENT_COLOR}",
                    },
                ),
            ),
            width="15em",
            padding_top="0.75em",
        ),
        rx.box(
            rx.cond(
                pysaas.DashState.show_profile_error,
                rx.wrap(
                    rx.text(
                        pysaas.DashState.profile_error_message,
                        font_size="0.8em",
                        color="#DC143C",
                        font_weight="330",
                        padding_top="0.5em",
                    ),
                ),
            ),
        ),
        rx.box(
            rx.button(
                "Update Profile",
                on_click=pysaas.DashState.update_user_data,
                bg="black",
                box_shadow=styles.DOC_SHADOW_LIGHT,
                color="white",
                margin_top=0,
                size="sm",
                border="2px solid black",
                _hover={
                    "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                },
                width="100%",
            ),
            width="14em",
            padding_top="2em",
        ),
        rx.alert_dialog(
            rx.alert_dialog_overlay(
                rx.alert_dialog_content(
                    rx.alert_dialog_header(pysaas.DashState.alert_heading),
                    rx.alert_dialog_body(
                        pysaas.DashState.alert_message,
                    ),
                    rx.alert_dialog_footer(
                        rx.button(
                            pysaas.DashState.close_button_message,
                            on_click=pysaas.DashState.toggle_alert,
                        )
                    ),
                )
            ),
            is_open=pysaas.DashState.show_alert,
        ),
        style=styles.DASH_STYLES,
        padding_bottom="2.5em",
    )


def update_password() -> rx.Component:
    return rx.box(
        rx.heading(
            "Update Password",
            font_weight="500",
            font_size="1.2em",
            padding_bottom="1em",
        ),
        rx.box(
            rx.text(
                "Current Password",
                font_size="0.85em",
                padding_bottom="0.1em",
                color="#676767",
            ),
            rx.password(
                placeholder="Password",
                on_blur=pysaas.DashState.set_password,
                color="black",
                type="email",
                size="md",
                border="2px solid #f4f4f4",
                box_shadow="rgba(0, 0, 0, 0.08) 0px 4px 12px",
                bg="rgba(255,255,255,.5)",
                _focus={
                    "border": f"2px solid {styles.ACCENT_COLOR}",
                },
            ),
            width="14em",
        ),
        rx.box(
            rx.cond(
                pysaas.DashState.show_email_error,
                rx.wrap(
                    rx.text(
                        pysaas.DashState.email_error_message,
                        font_size="0.8em",
                        color="#DC143C",
                        font_weight="330",
                        padding_top="0.5em",
                    ),
                ),
            ),
        ),
        rx.box(
            rx.button(
                "Send Reset Email",
                on_click=pysaas.DashState.send_password_reset,
                bg="black",
                box_shadow=styles.DOC_SHADOW_LIGHT,
                color="white",
                margin_top=0,
                size="sm",
                border="2px solid black",
                _hover={
                    "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                },
                width="100%",
            ),
            _hover={"text_decoration": "none"},
            width="14em",
            padding_top="2em",
        ),
        rx.alert_dialog(
            rx.alert_dialog_overlay(
                rx.alert_dialog_content(
                    rx.alert_dialog_header(pysaas.DashState.alert_heading),
                    rx.alert_dialog_body(
                        pysaas.DashState.alert_message,
                    ),
                    rx.alert_dialog_footer(
                        rx.button(
                            pysaas.DashState.close_button_message,
                            on_click=pysaas.DashState.toggle_alert,
                        )
                    ),
                )
            ),
            is_open=pysaas.DashState.show_alert,
        ),
        style=styles.DASH_STYLES,
        padding_bottom="2.5em",
    )


def tabs() -> rx.Component:
    return rx.tabs(
        rx.tab_list(
            rx.tab("Dashboard"),
            rx.tab("Subscription"),
            rx.tab("Settings"),
            padding_left="1em",
        ),
        rx.tab_panels(
            rx.tab_panel(
                dash_heading(),
                selector(),
                data_table(),
                padding_x="1.75em",
            ),
            rx.tab_panel(
                sub_heading(),
                sub_management(),
                padding_x="1.75em",
            ),
            rx.tab_panel(
                rx.box(
                    rx.heading(
                        "Settings",
                        font_weight="500",
                        font_size="1.75em",
                    ),
                    rx.text(
                        "Update your account details",
                        font_weight="349",
                        padding_top="0.3em",
                    ),
                ),
                rx.tabs(
                    rx.tab_list(
                        rx.tab("Account"),
                        rx.tab("Password"),
                    ),
                    rx.tab_panels(
                        rx.tab_panel(
                            account_profile(),
                        ),
                        rx.tab_panel(
                            update_password(),
                        ),
                        padding_top="0.75em",
                    ),
                    color="black",
                    width="100%",
                    padding_top="0.75em",
                ),
                width="100%",
                padding_x="1.75em",
            ),
        ),
        color="black",
        width="100%",
    )