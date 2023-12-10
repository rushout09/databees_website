import reflex as rx

from pysaas import styles


def error() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.image(
                src="/search.svg",
                width="4em",
            ),
            rx.heading(
                "Page not found",
                font_size=styles.H1_FONT_SIZE,
                font_weight="700",
            ),
            rx.text(
                "The page you are looking for does not exist.",
                color="#999999",
            ),
            rx.link(
                rx.button(
                    "Home",
                    bg="black",
                    box_shadow=styles.DOC_SHADOW_LIGHT,
                    color="white",
                    margin_top=0,
                    size="md",
                    border="2px solid black",
                    _hover={
                        "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                    },
                    width="8em",
                ),
                href="/",
                padding_top="1em",
            ),
            align_items="center",
        ),
        padding_top="10%",
    )