import reflex as rx

from pysaas import styles
from pysaas import pysaas


def signup_form() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.center(
                rx.vstack(
                    rx.link(
                        rx.hstack(
                            rx.image(
                                src="/logo.svg",
                                height="1.7em",
                                width="1.7em",
                            ),
                            rx.heading("PySaaS", font_size="1.7em"),
                        ),
                        href="/",
                        _hover={"text_decoration": "none"},
                    ),
                    rx.box(
                        rx.text("Create an account"),
                        padding_bottom="1em",
                        font_weight="330",
                    ),
                    rx.input(
                        on_blur=pysaas.AuthState.set_email, 
                        placeholder="Email", 
                        width="100%",
                    ),
                    rx.password(
                        on_blur=pysaas.AuthState.set_password,
                        placeholder="Password",
                        width="100%",
                    ),
                    rx.password(
                        on_blur=pysaas.AuthState.set_confirm_password,
                        placeholder="Confirm Password",
                        width="100%",
                    ),
                    rx.box(
                        rx.cond(
                            pysaas.AuthState.show_error,
                            rx.wrap(
                                rx.text(
                                    pysaas.AuthState.error_message,
                                    font_size="0.8em",
                                    color="#DC143C",
                                    font_weight="330",
                                ),
                            ),
                        ),
                    ),
                    rx.box(
                        rx.button(
                            "Sign up", 
                            on_click=pysaas.AuthState.signup, 
                            width="100%",
                            bg="black",
                            box_shadow=styles.DOC_SHADOW_LIGHT,
                            color="white",
                            margin_top=0,
                            size="md",
                            border="2px solid black",
                            _hover={
                                "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                            },
                        ),
                        padding_top="1em",
                        width="100%",
                    ),
                    rx.box(
                        rx.text(
                            "Already have an account? ",
                            rx.span(
                                rx.link(
                                    "Sign in →",
                                    href="/signin",
                                    color=styles.ACCENT_COLOR,
                                ),
                            ),
                        ),
                        font_size="0.8em",
                        padding_y="1em",
                    ),
                    width="87.5%",
                    padding_x="1em",
                ),
                width="65%",
                min_height="30em",
                style=styles.SIGNIN_INPUT_STYLES,
            ),
        ),
        style=styles.SIGNIN_PAGE_STYLES,
    )


def signin_form() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.center(
                rx.vstack(
                    rx.link(
                        rx.hstack(
                            rx.image(
                                src="/logo.svg",
                                height="1.7em",
                                width="1.7em",
                            ),
                            rx.heading("PySaaS", font_size="1.7em"),
                        ),
                        href="/",
                        _hover={"text_decoration": "none"},
                    ),
                    rx.box(
                        rx.text("Sign in to an account"),
                        padding_bottom="1em",
                        font_weight="330",
                    ),
                    rx.input(
                        on_blur=pysaas.AuthState.set_email, 
                        placeholder="Email", 
                        width="100%",
                    ),
                    rx.password(
                        on_blur=pysaas.AuthState.set_password,
                        placeholder="Password",
                        width="100%",
                    ),
                    rx.box(
                        rx.cond(
                            pysaas.AuthState.show_error,
                            rx.wrap(
                                rx.text(
                                    pysaas.AuthState.error_message,
                                    font_size="0.8em",
                                    color="#DC143C",
                                    font_weight="330",
                                ),
                            ),
                        ),
                    ),
                    rx.box(
                        rx.button(
                            "Sign in", 
                            on_click=pysaas.AuthState.signin, 
                            width="100%",
                            bg="black",
                            box_shadow=styles.DOC_SHADOW_LIGHT,
                            color="white",
                            margin_top=0,
                            size="md",
                            border="2px solid black",
                            _hover={
                                "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                            },
                        ),
                        padding_top="1em",
                        width="100%",
                    ),
                    rx.box(
                        rx.text(
                            "Don't have an account yet? ",
                            rx.span(
                                rx.link(
                                    "Sign up →",
                                    href="/signup",
                                    color=styles.ACCENT_COLOR,
                                ),
                            ),
                        ),
                        font_size="0.8em",
                        padding_y="1em",
                    ),
                    width="87.5%",
                    padding_x="1em",
                ),
                width="65%",
                min_height="30em",
                style=styles.SIGNIN_INPUT_STYLES,
            ),
        ),
        style=styles.SIGNIN_PAGE_STYLES,
    )