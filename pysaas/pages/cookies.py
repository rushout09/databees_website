import reflex as rx

from pysaas.components.navbar import navbar
from pysaas.components.footer import footer
from pysaas.components.cookies_content import cookies_content


def cookies() -> rx.Component:
    return rx.center(
        rx.vstack(
            navbar(),
            cookies_content(),
            footer(),
        ),
    )