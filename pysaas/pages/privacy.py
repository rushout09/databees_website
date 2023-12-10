import reflex as rx

from pysaas.components.navbar import navbar
from pysaas.components.footer import footer
from pysaas.components.privacy_content import privacy_content


def privacy() -> rx.Component:
    return rx.center(
        rx.vstack(
            navbar(),
            privacy_content(),
            footer(),
        ),
    )
