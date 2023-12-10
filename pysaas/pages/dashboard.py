import reflex as rx

from pysaas import pysaas
from pysaas.components.navbar import navbar
from pysaas.components.tabs import tabs


def dashboard() -> rx.Component:
    return rx.center(
        rx.cond(
            pysaas.State.signed_out,
            rx.box(),
            rx.vstack(
                navbar(),
                tabs(),
                padding_bottom="1em",
                width="100%",
            ),
        ),
    )