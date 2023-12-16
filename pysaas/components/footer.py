import reflex as rx

from pysaas import styles
from pysaas import pysaas
from pysaas.components.logo import logo


def footer() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.desktop_only(
                    rx.link(logo(**styles.LOGO_FOOTER_STYLE), href="/"),
                ),
                rx.vstack(
                    rx.text("Product", color=styles.DOC_REG_TEXT_COLOR),
                    rx.link("Features", href="/#features", style=styles.FOOTER_ITEM_STYLE),
                    # rx.link("Pricing", href="/#pricing", style=styles.FOOTER_ITEM_STYLE),
                    rx.link("Blog", href="/blog", style=styles.FOOTER_ITEM_STYLE),
                    align_items="start",
                ),
                rx.vstack(
                    rx.text("Social", color=styles.DOC_REG_TEXT_COLOR),
                    rx.link(
                        "LinkedIn",
                        href="/",
                        style=styles.FOOTER_ITEM_STYLE,
                    ),
                    rx.link(
                        "Contact Us",
                        href="mailto: hello@databees.work",
                        style=styles.FOOTER_ITEM_STYLE,
                    ),
                    rx.link(
                        "GitHub",
                        href="https://github.com/rushout09/databees_website",
                        style=styles.FOOTER_ITEM_STYLE,
                    ),
                    align_items="start",
                ),
                rx.vstack(
                    rx.text("Legal", color=styles.DOC_REG_TEXT_COLOR),
                    rx.link(
                        "Terms & Conditions",
                        href="/terms",
                        style=styles.FOOTER_ITEM_STYLE,
                    ),
                    rx.link(
                        "Privacy Policy",
                        href="/privacy",
                        style=styles.FOOTER_ITEM_STYLE,
                    ),
                    rx.link("Cookie Policy",
                        href="/cookies",
                        style=styles.FOOTER_ITEM_STYLE
                    ),
                    align_items="start",
                ),
                justify="space-between",
                color=styles.LIGHT_TEXT_COLOR,
                align_items="top",
                padding_bottom="3em",
                min_width="100%",
            ),
            rx.hstack(
                rx.text(
                    "Artificial Intelligence for the Real World",
                    font_weight="500",
                ),
                justify="center",
                color=styles.LIGHT_TEXT_COLOR,
                padding_bottom="2em",
                min_width="100%",
            ),
            padding_top="10%",
        ),
        width="85%",
    )


def blog_footer() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.desktop_only(
                    rx.cond(
                        ~pysaas.State.show_spinner,
                        rx.link(logo(**styles.LOGO_FOOTER_STYLE), href="/"),
                    ),
                ),
                rx.cond(
                    ~pysaas.State.show_spinner,
                    rx.vstack(
                        rx.text("Product", color=styles.DOC_REG_TEXT_COLOR),
                        rx.link("Features", href="/#features", style=styles.FOOTER_ITEM_STYLE),
                        # rx.link("Pricing", href="/#pricing", style=styles.FOOTER_ITEM_STYLE),
                        rx.link("Blog", href="/blog", style=styles.FOOTER_ITEM_STYLE),
                        align_items="start",
                    ),
                ),
                rx.cond(
                    ~pysaas.State.show_spinner,
                    rx.vstack(
                        rx.text("Social", color=styles.DOC_REG_TEXT_COLOR),
                        rx.link(
                            "LinkedIn",
                            href="/",
                            style=styles.FOOTER_ITEM_STYLE,
                        ),
                        rx.link(
                            "Contact Us",
                            href="mailto: hello@databees.work",
                            style=styles.FOOTER_ITEM_STYLE,
                        ),
                        rx.link(
                            "GitHub",
                            href="https://github.com/rushout09/databees_website",
                            style=styles.FOOTER_ITEM_STYLE,
                        ),
                        align_items="start",
                    ),
                ),
                rx.cond(
                    ~pysaas.State.show_spinner,
                    rx.vstack(
                        rx.text("Legal", color=styles.DOC_REG_TEXT_COLOR),
                        rx.link(
                            "Terms & Conditions",
                            href="/terms",
                            style=styles.FOOTER_ITEM_STYLE,
                        ),
                        rx.link(
                            "Privacy Policy",
                            href="/privacy",
                            style=styles.FOOTER_ITEM_STYLE,
                        ),
                        rx.link(
                            "Cookie Policy",
                            href="/cookies",
                            style=styles.FOOTER_ITEM_STYLE
                        ),
                        align_items="start",
                    ),
                ),
                justify="space-between",
                color=styles.LIGHT_TEXT_COLOR,
                align_items="top",
                padding_bottom="3em",
                min_width="100%",
            ),
            rx.cond(
                ~pysaas.State.show_spinner,
                rx.hstack(
                    rx.text(
                        "Artificial Intelligence for the Real World",
                        font_weight="500",
                    ),
                    justify="center",
                    color=styles.LIGHT_TEXT_COLOR,
                    padding_bottom="2em",
                    min_width="100%",
                ),
            ),
            padding_top="10%",
        ),
        width="85%",
    )
