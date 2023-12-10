import reflex as rx

from pysaas.components.userauth import signin_form


def signin() -> rx.Component:
    return rx.center(
        rx.vstack(
            signin_form(),
            width="100%",
        ),
    )