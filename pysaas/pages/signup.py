import reflex as rx

from pysaas.components.userauth import signup_form


def signup() -> rx.Component:
    return rx.center(
        rx.vstack(
            signup_form(),
            width="100%",
        ),
    )