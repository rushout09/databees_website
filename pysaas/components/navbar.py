import reflex as rx

from pysaas import styles
from pysaas import pysaas
from pysaas.components.logo import logo


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.link(
                rx.hstack(
                    logo(**styles.LOGO_NAV_STYLE),
                    rx.tablet_and_desktop(
                        rx.text(
                            "DataBees",
                            font_size=styles.H3_FONT_SIZE,
                            font_weight=600,
                        ),
                    ),
                    spacing="0.25em",
                ),
                href="/",
                _hover={"text_decoration": "none"},
            ),
            rx.cond(
                pysaas.State.signed_out,
                rx.hstack(
                    rx.tablet_and_desktop(
                        rx.link(
                            rx.text(
                                "Features",
                            ),
                            href="/#features",
                            **styles.BUTTON_STYLE,
                        ),
                    ),
                    rx.tablet_and_desktop(
                        rx.link(
                            rx.text(
                                "Pricing",
                            ),
                            href="/#pricing",
                            **styles.BUTTON_STYLE,
                        ),
                    ),
                    rx.tablet_and_desktop(
                        rx.link(
                            rx.text(
                                "Blog",
                            ),
                            href="/blog",
                            **styles.BUTTON_STYLE,
                        ),
                    ),
                    rx.link(
                        rx.button(
                            "Sign in",
                            bg=styles.DOC_TEXT_COLOR,
                            box_shadow=styles.DOC_SHADOW_LIGHT,
                            color="white",
                            margin_top=0,
                            size="sm",
                            border="2px solid black",
                            _hover={
                                "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                            },
                        ),
                        href="/signin",
                        _hover={"text_decoration": "none"},
                    ),
                    spacing="1em",
                ),
                rx.box(
                    rx.hstack(
                        rx.cond(
                            ~pysaas.State.plan,
                            rx.tooltip(
                                rx.badge(
                                    "Free Plan", variant="subtle", color_scheme="green"
                                ),
                                label="You're on a free plan. Upgrade at any time.",
                            ),
                        ),
                        rx.popover(
                            rx.popover_trigger(
                                rx.button(
                                    rx.avatar(size="sm"),
                                    background="transparent",
                                    padding_x="0",
                                    style={"_hover": {"background": "transparent"}},
                                ),
                            ),
                            rx.popover_content(
                                rx.popover_header(
                                    rx.text(
                                        "Signed in as ",
                                        rx.span(
                                            rx.text(
                                                pysaas.State.get_user_email,
                                                font_size="0.85em",
                                                color="black",
                                                font_weight="400",
                                            ),
                                        ),
                                        font_size="0.85em",
                                        color="#606060"
                                    ),
                                ),
                                rx.link(
                                    rx.popover_body(
                                        rx.hstack(
                                            rx.image(
                                                src="/dashboard.svg",
                                                width="1em",
                                            ),
                                            rx.text("Dashboard"),
                                        ),
                                        _hover={
                                            "background_color": "#f8f8f8",
                                        },
                                    ),
                                    href="/dashboard",
                                    _hover={
                                        "text_decoration": "none",
                                    },
                                ),
                                rx.link(
                                    rx.popover_body(
                                        rx.hstack(
                                            rx.image(
                                                src="/signout.svg",
                                                width="1em",
                                            ),
                                            rx.text("Sign out"),
                                        ),
                                        _hover={
                                            "background_color": "#f8f8f8",
                                        },
                                    ),
                                    href="/signout",
                                    _hover={
                                        "text_decoration": "none",
                                    },
                                ),
                            ),
                            close_on_blur=True,
                        ),
                        spacing="1em",
                    ),
                ),
            ),
            justify="space-between",
            padding_x=styles.PADDING_X,
        ),
        backdrop_filter="blur(10px)",
        padding_y=["0.8em", "0.8em", "0.5em"],
        border_bottom="0.05em solid rgba(100, 116, 139, .2)",
        position="sticky",
        width="100%",
        top="0px",
        z_index="99",
    )