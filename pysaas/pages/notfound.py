import reflex as rx

from pysaas.components.navbar import navbar
from pysaas.components.error import error


def not_found() -> rx.Component:
    return rx.center(
        rx.vstack(
            navbar(),
            error(),
            width="100%",
        ),
    )