import reflex as rx

from pysaas.components.navbar import navbar
from pysaas.components.footer import footer
from pysaas.components.terms_content import terms_content


def terms() -> rx.Component:
    return rx.center(
        rx.vstack(
            navbar(),
            terms_content(),
            footer(),
        ),
    )
