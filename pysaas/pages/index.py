import reflex as rx

from pysaas.components.navbar import navbar
from pysaas.components.landing import hero, features, pricing, cta
from pysaas.components.footer import footer


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            navbar(),
            hero(),
            features(),
            pricing(),
            cta(),
            footer(),
            width="100%",
        ),
    )