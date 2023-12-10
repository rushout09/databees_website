import reflex as rx

from pysaas import styles
from pysaas import pysaas


def hero() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.tablet_and_desktop(
                    rx.text(
                        "Collect and Curate Datasets faster with",
                        font_size="2em",
                        font_weight=700,
                    ),
                    rx.text(
                        "DataBees",
                        font_size="2em",
                        font_weight=800,
                        background_image="linear-gradient(371.68deg, #7F00FF  25%, #6495ED 50%)",
                        background_clip="text",
                    ),
                    text_align="center",
                    # line_height="1.15",
                ),
                rx.mobile_only(
                    rx.text(
                        "Ship faster with",
                        font_size="1.5em",
                        font_weight=700,
                    ),
                    rx.text(
                        "PySaaS",
                        font_size="1.5em",
                        font_weight=800,
                        background_image="linear-gradient(371.68deg, #7F00FF  25%, #6495ED 50%)",
                        background_clip="text",
                    ),
                    text_align="center",
                    # line_height="1.15",
                ),
            ),
            rx.container(
                "Welcome to your new landing page, built in pure Python.",
                color="grey",
                font_size="0.6em",
                text_align="center",
            ),
            rx.hstack(
                rx.cond(
                    pysaas.State.signed_out,
                    rx.link(
                        rx.button(
                            "Get Started ›",
                            bg="black",
                            box_shadow=styles.DOC_SHADOW_LIGHT,
                            color="white",
                            margin_top=0,
                            size="md",
                            border="2px solid black",
                            _hover={
                                "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                            },
                        ),
                        href="/signup",
                    ),
                    rx.link(
                        rx.button(
                            "Get Started ›",
                            bg="black",
                            box_shadow=styles.DOC_SHADOW_LIGHT,
                            color="white",
                            margin_top=0,
                            size="md",
                            border="2px solid black",
                            _hover={
                                "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                            },
                        ),
                        href="/dashboard",
                    ),
                ),
                rx.link(
                    rx.button(
                        "View Pricing",
                        bg="white",
                        box_shadow=styles.DOC_SHADOW_LIGHT,
                        color="black",
                        margin_top=0,
                        size="md",
                        border="2px solid black",
                        _hover={
                            "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                        },
                    ),
                    href="/#pricing",
                    _hover={
                        "text_decoration": "none",
                    }
                ),
                justify="center",
                should_wrap_children=True,
                spacing="0.2em",
            ),
            spacing="1em",
            font_size="2em",
        ),
        padding_top="7.5%"
    )


def features() -> rx.Component:
    return rx.box(
        rx.tablet_and_desktop(
            rx.text(
                "Features",
                font_size="2em",
                font_weight=700,
            ),
            text_align="center",
            line_height="1.15",
            padding_bottom="0.5em",
        ),
        rx.mobile_only(
            rx.text(
                "Features",
                font_size="1.5em",
                font_weight=700,
            ),
            text_align="center",
            line_height="1.15",
            padding_bottom="0.5em",
        ),
        rx.container(
            "Focus on delivering value to customers and generating revenue.",
            color="grey",
            font_size="1.25em",
            text_align="center",
            padding_bottom="1.5em"
        ),
        rx.tablet_and_desktop(
            rx.center(
                rx.vstack(
                    rx.hstack(
                        rx.box(
                            rx.vstack(
                                rx.image(
                                    src="/user.svg",
                                    height="2em",
                                    width="2em",
                                ),
                                rx.text(
                                    "Authentication",
                                    font_size=styles.H2_FONT_SIZE,
                                    font_weight=styles.BOLD_WEIGHT,
                                    color="black",
                                ),
                                rx.text(
                                    "PySaaS supports Firebase authentication and real-time database, allowing multiple users to see changes when data is created or edited.",
                                    color="#676767",
                                ),
                                margin_bottom="1em",
                                style=styles.BOX_STYLES,
                                height="18em",
                                width="22em",
                                padding_top="2em",
                            ),
                        ),
                        rx.box(
                            rx.vstack(
                                rx.image(
                                    src="/card.svg",
                                    height="2em",
                                    width="2em",
                                ),
                                rx.text(
                                    "Subscriptions",
                                    font_size=styles.H2_FONT_SIZE,
                                    font_weight=styles.BOLD_WEIGHT,
                                    color="black",
                                ),
                                rx.text(
                                    "Let customers manage billing settings directly in your app, and remove the headache of tax compliance by using Lemon Squeezy as a MoR.",
                                    color="#676767",
                                ),
                                margin_bottom="1em",
                                style=styles.BOX_STYLES,
                                height="18em",
                                width="22em",
                                padding_top="2em",
                            ),
                        ),
                        spacing="1em",
                        width="100%",
                    ),
                    rx.hstack(
                        rx.box(
                            rx.vstack(
                                rx.image(
                                    src="/blog.svg",
                                    height="2em",
                                    width="2em",
                                ),
                                rx.text(
                                    "Notion CMS",
                                    font_size=styles.H2_FONT_SIZE,
                                    font_weight=styles.BOLD_WEIGHT,
                                    color="black",
                                ),
                                rx.text(
                                    "A simple publishing system is critical to consistent content creation. Now, you can publish blog posts directly from your Notion database.",
                                    color="#676767",
                                ),
                                margin_bottom="1em",
                                style=styles.BOX_STYLES,
                                height="18em",
                                width="22em",
                                padding_top="2em",
                            ),
                        ),
                        rx.box(
                            rx.vstack(
                                rx.image(
                                    src="/art.svg",
                                    height="2em",
                                    width="2em",
                                ),
                                rx.text(
                                    "UI Styling",
                                    font_size=styles.H2_FONT_SIZE,
                                    font_weight=styles.BOLD_WEIGHT,
                                    color="black",
                                ),
                                rx.text(
                                    "Don't worry about fancy styling libraries if that isn't your thing. Create beautiful UI components with ease using Python functions instead.",
                                    color="#676767",
                                ),
                                margin_bottom="1em",
                                style=styles.BOX_STYLES,
                                height="18em",
                                width="22em",
                                padding_top="2em",
                            ),
                        ),
                        spacing="1em",
                        width="100%",
                    ),
                    rx.hstack(
                        rx.box(
                            rx.vstack(
                                rx.image(
                                    src="/cloud.svg",
                                    height="2em",
                                    width="2em",
                                ),
                                rx.text(
                                    "Hosting",
                                    font_size=styles.H2_FONT_SIZE,
                                    font_weight=styles.BOLD_WEIGHT,
                                    color="black",
                                ),
                                rx.text(
                                    "Deploy to an existing cloud provider of your choice by simply editing a configuration file to match the IP address of your server.",
                                    color="#676767",
                                ),
                                margin_bottom="1em",
                                style=styles.BOX_STYLES,
                                height="18em",
                                width="22em",
                                padding_top="2em",
                            ),
                        ),
                        rx.box(
                            rx.vstack(
                                rx.image(
                                    src="/python.svg",
                                    height="2em",
                                    width="2em",
                                ),
                                rx.text(
                                    "Pure Python",
                                    font_size=styles.H2_FONT_SIZE,
                                    font_weight=styles.BOLD_WEIGHT,
                                    color="black",
                                ),
                                rx.text(
                                    "Gone are the days of learning countless languages and frameworks. Build your frontend and backend, everything in pure Python.",
                                    color="#676767",
                                ),
                                margin_bottom="1em",
                                style=styles.BOX_STYLES,
                                height="18em",
                                width="22em",
                                padding_top="2em",
                            ),
                        ),
                        spacing="1em",
                        width="100%",
                    ),
                ),
            ),
        ),
        rx.mobile_only(
            rx.vstack(
                rx.box(
                    rx.vstack(
                        rx.image(
                            src="/user.svg",
                            height="2em",
                            width="2em",
                        ),
                        rx.text(
                            "Authentication",
                            font_size=styles.H2_FONT_SIZE,
                            font_weight=styles.BOLD_WEIGHT,
                            color="black",
                        ),
                        rx.text(
                            "PySaaS supports Firebase authentication and real-time database, allowing multiple users to see changes when data is created or edited.",
                            color="#676767",
                        ),
                        margin_bottom="1em",
                        style=styles.BOX_STYLES,
                        min_height="15em",
                    ),
                ),
                rx.box(
                    rx.vstack(
                        rx.image(
                            src="/card.svg",
                            height="2em",
                            width="2em",
                        ),
                        rx.text(
                            "Subscriptions",
                            font_size=styles.H2_FONT_SIZE,
                            font_weight=styles.BOLD_WEIGHT,
                            color="black",
                        ),
                        rx.text(
                            "Let customers manage billing settings directly in your app, and remove the headache of tax compliance by using Lemon Squeezy as a MoR.",
                            color="#676767",
                        ),
                        margin_bottom="1em",
                        style=styles.BOX_STYLES,
                        min_height="15em",
                    ),
                ),
                rx.box(
                    rx.vstack(
                        rx.image(
                            src="/blog.svg",
                            height="2em",
                            width="2em",
                        ),
                        rx.text(
                            "Notion CMS",
                            font_size=styles.H2_FONT_SIZE,
                            font_weight=styles.BOLD_WEIGHT,
                            color="black",
                        ),
                        rx.text(
                            "A simple publishing system is critical to consistent content creation. Now, you can publish blog posts directly from your Notion database.",
                            color="#676767",
                        ),
                        margin_bottom="1em",
                        style=styles.BOX_STYLES,
                        min_height="15em",
                    ),
                ),
                rx.box(
                    rx.vstack(
                        rx.image(
                            src="/art.svg",
                            height="2em",
                            width="2em",
                        ),
                        rx.text(
                            "UI Styling",
                            font_size=styles.H2_FONT_SIZE,
                            font_weight=styles.BOLD_WEIGHT,
                            color="black",
                        ),
                        rx.text(
                            "Don't worry about fancy styling libraries if that isn't your thing. Create beautiful UI components with ease using Python functions instead.",
                            color="#676767",
                        ),
                        margin_bottom="1em",
                        style=styles.BOX_STYLES,
                        min_height="15em",
                    ),
                ),
                rx.box(
                    rx.vstack(
                        rx.image(
                            src="/cloud.svg",
                            height="2em",
                            width="2em",
                        ),
                        rx.text(
                            "Hosting",
                            font_size=styles.H2_FONT_SIZE,
                            font_weight=styles.BOLD_WEIGHT,
                            color="black",
                        ),
                        rx.text(
                            "Deploy to an existing cloud provider of your choice by simply editing a configuration file to match the IP address of your server.",
                            color="#676767",
                        ),
                        margin_bottom="1em",
                        style=styles.BOX_STYLES,
                        min_height="15em",
                    ),
                ),
                rx.box(
                    rx.vstack(
                        rx.image(
                            src="/python.svg",
                            height="2em",
                            width="2em",
                        ),
                        rx.text(
                            "Pure Python",
                            font_size=styles.H2_FONT_SIZE,
                            font_weight=styles.BOLD_WEIGHT,
                            color="black",
                        ),
                        rx.text(
                            "Gone are the days of learning countless languages and frameworks. Build your frontend and backend, everything in pure Python.",
                            color="#676767",
                        ),
                        margin_bottom="1em",
                        style=styles.BOX_STYLES,
                        min_height="15em",
                    ),
                ),
                spacing="1em",
            ),
        ),
        padding_top="10%",
        width="70%",
        id="features",
    )


def pricing_cards() -> rx.Component:
    return rx.box(
        rx.center(
            rx.hstack(
                rx.text("Monthly"),
                rx.switch(
                    is_checked=pysaas.IndexState.yearly_pricing,
                    on_change=pysaas.IndexState.toggle_pricing,
                ),
                rx.text("Yearly ",),
            ),
            padding_bottom="1.5em",
        ),
        rx.tablet_and_desktop(
            rx.hstack(
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Pro",
                            font_size=styles.H3_FONT_SIZE,
                            font_weight=styles.BOLD_WEIGHT,
                            color="black",
                        ),
                        rx.text(
                            "Description of your Pro plan.",
                            color="#676767",
                        ),
                        rx.text(
                            rx.span(
                                rx.cond(
                                    pysaas.IndexState.yearly_pricing,
                                    pysaas.IndexState.pro_yr,
                                    pysaas.IndexState.pro_mo,
                                ),
                                font_size=styles.H2_FONT_SIZE,
                                font_weight=styles.BOLD_WEIGHT,
                                color="black",
                            ),
                            rx.cond(
                                pysaas.IndexState.yearly_pricing,
                                " / year",
                                " / month",
                            ),
                            font_size=styles.H4_FONT_SIZE,
                        ),
                        rx.list(
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            spacing="0.5em",
                            padding_top="0.5em",
                            color="#676767",
                        ),
                        rx.box(
                            rx.cond(
                                pysaas.State.signed_out,
                                rx.link(
                                    rx.button(
                                        "Get Started",
                                        bg="black",
                                        box_shadow=styles.DOC_SHADOW_LIGHT,
                                        color="white",
                                        margin_top=0,
                                        size="md",
                                        border="2px solid black",
                                        _hover={
                                            "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                                        },
                                        width="100%",
                                    ),
                                    href="/signup",
                                ),
                                rx.link(
                                    rx.button(
                                        "Get Started",
                                        bg="black",
                                        box_shadow=styles.DOC_SHADOW_LIGHT,
                                        color="white",
                                        margin_top=0,
                                        size="md",
                                        border="2px solid black",
                                        _hover={
                                            "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                                        },
                                        width="100%",
                                    ),
                                    href="/dashboard",
                                ),
                            ),
                            padding_top="2em",
                        ),
                        margin_bottom="1em",
                        style=styles.BOX_STYLES,
                        min_height="30em",
                        max_width="17em",
                    ),
                ),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Premium ",
                            rx.span(
                                rx.badge(
                                    "Most Popular", variant="subtle", color_scheme="green"
                                ),
                            ),
                            font_size=styles.H3_FONT_SIZE,
                            font_weight=styles.BOLD_WEIGHT,
                            color="black",
                        ),
                        rx.text(
                            "Description of your Premium plan.",
                            color="#676767",
                        ),
                        rx.text(
                            rx.span(
                                rx.cond(
                                    pysaas.IndexState.yearly_pricing,
                                    pysaas.IndexState.premium_yr,
                                    pysaas.IndexState.premium_mo,
                                ),
                                font_size=styles.H2_FONT_SIZE,
                                font_weight=styles.BOLD_WEIGHT,
                                color="black",
                            ),
                            rx.cond(
                                pysaas.IndexState.yearly_pricing,
                                " / year",
                                " / month",
                            ),
                            font_size=styles.H4_FONT_SIZE,
                        ),
                        rx.list(
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            spacing="0.5em",
                            padding_top="0.5em",
                            color="#676767",
                        ),
                        rx.box(
                            rx.cond(
                                pysaas.State.signed_out,
                                rx.link(
                                    rx.button(
                                        "Get Started",
                                        bg="black",
                                        box_shadow=styles.DOC_SHADOW_LIGHT,
                                        color="white",
                                        margin_top=0,
                                        size="md",
                                        border="2px solid black",
                                        _hover={
                                            "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                                        },
                                        width="100%",
                                    ),
                                    href="/signup",
                                ),
                                    rx.link(
                                    rx.button(
                                        "Get Started",
                                        bg="black",
                                        box_shadow=styles.DOC_SHADOW_LIGHT,
                                        color="white",
                                        margin_top=0,
                                        size="md",
                                        border="2px solid black",
                                        _hover={
                                            "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                                        },
                                        width="100%",
                                    ),
                                    href="/dashboard",
                                ),
                            ),
                            padding_top="2em",
                        ),
                        margin_bottom="1em",
                        style=styles.POPULAR_PRICE_STYLES,
                        min_height="30em",
                        max_width="17em",
                    ),
                ),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Enterprise",
                            font_size=styles.H3_FONT_SIZE,
                            font_weight=styles.BOLD_WEIGHT,
                            color="black",
                        ),
                        rx.text(
                            "Description of your Enterprise plan.",
                            color="#676767",
                        ),
                        rx.text(
                            rx.span(
                                rx.cond(
                                    pysaas.IndexState.yearly_pricing,
                                    pysaas.IndexState.enterprise_yr,
                                    pysaas.IndexState.enterprise_mo,
                                ),
                                font_size=styles.H2_FONT_SIZE,
                                font_weight=styles.BOLD_WEIGHT,
                                color="black",
                            ),
                            rx.cond(
                                pysaas.IndexState.yearly_pricing,
                                " / year",
                                " / month",
                            ),
                            font_size=styles.H4_FONT_SIZE,
                        ),
                        rx.list(
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            spacing="0.5em",
                            padding_top="0.5em",
                            color="#676767",
                        ),
                        rx.box(
                            rx.cond(
                                pysaas.State.signed_out,
                                rx.link(
                                    rx.button(
                                        "Get Started",
                                        bg="black",
                                        box_shadow=styles.DOC_SHADOW_LIGHT,
                                        color="white",
                                        margin_top=0,
                                        size="md",
                                        border="2px solid black",
                                        _hover={
                                            "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                                        },
                                        width="100%",
                                    ),
                                    href="/signup",
                                ),
                                rx.link(
                                    rx.button(
                                        "Get Started",
                                        bg="black",
                                        box_shadow=styles.DOC_SHADOW_LIGHT,
                                        color="white",
                                        margin_top=0,
                                        size="md",
                                        border="2px solid black",
                                        _hover={
                                            "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                                        },
                                        width="100%",
                                    ),
                                    href="/dashboard",
                                ),
                            ),
                            padding_top="2em",
                        ),
                        margin_bottom="1em",
                        style=styles.BOX_STYLES,
                        min_height="30em",
                        max_width="17em",
                    ),
                ),
                justify="center",
                spacing="1em",
            ),
        ),
        rx.mobile_only(
            rx.vstack(
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Pro",
                            font_size=styles.H3_FONT_SIZE,
                            font_weight=styles.BOLD_WEIGHT,
                            color="black",
                        ),
                        rx.text(
                            "Description of your Pro plan.",
                            color="#676767",
                        ),
                        rx.text(
                            rx.span(
                                rx.cond(
                                    pysaas.IndexState.yearly_pricing,
                                    pysaas.IndexState.pro_yr,
                                    pysaas.IndexState.pro_mo,
                                ),
                                font_size=styles.H2_FONT_SIZE,
                                font_weight=styles.BOLD_WEIGHT,
                                color="black",
                            ),
                            rx.cond(
                                pysaas.IndexState.yearly_pricing,
                                " / year",
                                " / month",
                            ),
                            font_size=styles.H4_FONT_SIZE,
                        ),
                        rx.list(
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            spacing="0.5em",
                            padding_top="0.5em",
                            color="#676767",
                        ),
                        rx.box(
                            rx.link(
                                rx.button(
                                    "Get Started",
                                    bg="black",
                                    box_shadow=styles.DOC_SHADOW_LIGHT,
                                    color="white",
                                    margin_top=0,
                                    size="md",
                                    border="2px solid black",
                                    _hover={
                                        "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                                    },
                                    width="100%",
                                ),
                                href="/signup",
                            ),
                            padding_top="2em",
                        ),
                        margin_bottom="1em",
                        style=styles.BOX_STYLES,
                        min_height="30em",
                    ),
                ),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Premium ",
                            rx.span(
                                rx.badge(
                                    "Most Popular", variant="subtle", color_scheme="green"
                                ),
                            ),
                            font_size=styles.H3_FONT_SIZE,
                            font_weight=styles.BOLD_WEIGHT,
                            color="black",
                        ),
                        rx.text(
                            "Description of your Premium plan.",
                            color="#676767",
                        ),
                        rx.text(
                            rx.span(
                                rx.cond(
                                    pysaas.IndexState.yearly_pricing,
                                    pysaas.IndexState.premium_yr,
                                    pysaas.IndexState.premium_mo,
                                ),
                                font_size=styles.H2_FONT_SIZE,
                                font_weight=styles.BOLD_WEIGHT,
                                color="black",
                            ),
                            rx.cond(
                                pysaas.IndexState.yearly_pricing,
                                " / year",
                                " / month",
                            ),
                            font_size=styles.H4_FONT_SIZE,
                        ),
                        rx.list(
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            spacing="0.5em",
                            padding_top="0.5em",
                            color="#676767",
                        ),
                        rx.box(
                            rx.link(
                                rx.button(
                                    "Get Started",
                                    bg="black",
                                    box_shadow=styles.DOC_SHADOW_LIGHT,
                                    color="white",
                                    margin_top=0,
                                    size="md",
                                    border="2px solid black",
                                    _hover={
                                        "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                                    },
                                    width="100%",
                                ),
                                href="/signup",
                            ),
                            padding_top="2em",
                        ),
                        margin_bottom="1em",
                        style=styles.POPULAR_PRICE_STYLES,
                        min_height="30em",
                    ),
                ),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Enterprise",
                            font_size=styles.H3_FONT_SIZE,
                            font_weight=styles.BOLD_WEIGHT,
                            color="black",
                        ),
                        rx.text(
                            "Description of your Enterprise plan.",
                            color="#676767",
                        ),
                        rx.text(
                            rx.span(
                                rx.cond(
                                    pysaas.IndexState.yearly_pricing,
                                    pysaas.IndexState.enterprise_yr,
                                    pysaas.IndexState.enterprise_mo,
                                ),
                                font_size=styles.H2_FONT_SIZE,
                                font_weight=styles.BOLD_WEIGHT,
                                color="black",
                            ),
                            rx.cond(
                                pysaas.IndexState.yearly_pricing,
                                " / year",
                                " / month",
                            ),
                            font_size=styles.H4_FONT_SIZE,
                        ),
                        rx.list(
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            spacing="0.5em",
                            padding_top="0.5em",
                            color="#676767",
                        ),
                        rx.box(
                            rx.link(
                                rx.button(
                                    "Get Started",
                                    bg="black",
                                    box_shadow=styles.DOC_SHADOW_LIGHT,
                                    color="white",
                                    margin_top=0,
                                    size="md",
                                    border="2px solid black",
                                    _hover={
                                        "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                                    },
                                    width="100%",
                                ),
                                href="/signup",
                            ),
                            padding_top="2em",
                        ),
                        margin_bottom="1em",
                        style=styles.BOX_STYLES,
                        min_height="30em",
                    ),
                ),
                justify="center",
                spacing="1em",
            ),
        ),
    )


def purchase_cards() -> rx.Component:
    return rx.box(
        rx.center(
            rx.hstack(
                rx.text("Monthly"),
                rx.switch(
                    is_checked=pysaas.IndexState.yearly_pricing,
                    on_change=pysaas.IndexState.toggle_pricing,
                ),
                rx.text("Yearly ",),
            ),
            padding_bottom="1.5em",
        ),
        rx.tablet_and_desktop(
            rx.hstack(
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Pro",
                            font_size=styles.H3_FONT_SIZE,
                            font_weight=styles.BOLD_WEIGHT,
                            color="black",
                        ),
                        rx.text(
                            "Description of your Pro plan.",
                            color="#676767",
                        ),
                        rx.text(
                            rx.span(
                                rx.cond(
                                    pysaas.IndexState.yearly_pricing,
                                    pysaas.IndexState.pro_yr,
                                    pysaas.IndexState.pro_mo,
                                ),
                                font_size=styles.H2_FONT_SIZE,
                                font_weight=styles.BOLD_WEIGHT,
                                color="black",
                            ),
                            rx.cond(
                                pysaas.IndexState.yearly_pricing,
                                " / year",
                                " / month",
                            ),
                            font_size=styles.H4_FONT_SIZE,
                        ),
                        rx.list(
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            spacing="0.5em",
                            padding_top="0.5em",
                            color="#676767",
                        ),
                        rx.box(
                            rx.link(
                                rx.button(
                                    "Checkout",
                                    bg="black",
                                    box_shadow=styles.DOC_SHADOW_LIGHT,
                                    color="white",
                                    margin_top=0,
                                    size="md",
                                    border="2px solid black",
                                    _hover={
                                        "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                                    },
                                    width="100%",
                                ),
                                href=pysaas.State.get_lm_url,
                            ),
                            padding_top="2em",
                        ),
                        margin_bottom="1em",
                        style=styles.BOX_STYLES,
                        min_height="30em",
                        max_width="17em",
                    ),
                ),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Premium ",
                            rx.span(
                                rx.badge(
                                    "Most Popular", variant="subtle", color_scheme="green"
                                ),
                            ),
                            font_size=styles.H3_FONT_SIZE,
                            font_weight=styles.BOLD_WEIGHT,
                            color="black",
                        ),
                        rx.text(
                            "Description of your Premium plan.",
                            color="#676767",
                        ),
                        rx.text(
                            rx.span(
                                rx.cond(
                                    pysaas.IndexState.yearly_pricing,
                                    pysaas.IndexState.premium_yr,
                                    pysaas.IndexState.premium_mo,
                                ),
                                font_size=styles.H2_FONT_SIZE,
                                font_weight=styles.BOLD_WEIGHT,
                                color="black",
                            ),
                            rx.cond(
                                pysaas.IndexState.yearly_pricing,
                                " / year",
                                " / month",
                            ),
                            font_size=styles.H4_FONT_SIZE,
                        ),
                        rx.list(
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            spacing="0.5em",
                            padding_top="0.5em",
                            color="#676767",
                        ),
                        rx.box(
                            rx.link(
                                rx.button(
                                    "Checkout",
                                    bg="black",
                                    box_shadow=styles.DOC_SHADOW_LIGHT,
                                    color="white",
                                    margin_top=0,
                                    size="md",
                                    border="2px solid black",
                                    _hover={
                                        "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                                    },
                                    width="100%",
                                ),
                                href=pysaas.State.get_lm_url,
                            ),
                            padding_top="2em",
                        ),
                        margin_bottom="1em",
                        style=styles.POPULAR_PRICE_STYLES,
                        min_height="30em",
                        max_width="17em",
                    ),
                ),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Enterprise",
                            font_size=styles.H3_FONT_SIZE,
                            font_weight=styles.BOLD_WEIGHT,
                            color="black",
                        ),
                        rx.text(
                            "Description of your Enterprise plan.",
                            color="#676767",
                        ),
                        rx.text(
                            rx.span(
                                rx.cond(
                                    pysaas.IndexState.yearly_pricing,
                                    pysaas.IndexState.enterprise_yr,
                                    pysaas.IndexState.enterprise_mo,
                                ),
                                font_size=styles.H2_FONT_SIZE,
                                font_weight=styles.BOLD_WEIGHT,
                                color="black",
                            ),
                            rx.cond(
                                pysaas.IndexState.yearly_pricing,
                                " / year",
                                " / month",
                            ),
                            font_size=styles.H4_FONT_SIZE,
                        ),
                        rx.list(
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            spacing="0.5em",
                            padding_top="0.5em",
                            color="#676767",
                        ),
                        rx.box(
                            rx.link(
                                rx.button(
                                    "Checkout",
                                    bg="black",
                                    box_shadow=styles.DOC_SHADOW_LIGHT,
                                    color="white",
                                    margin_top=0,
                                    size="md",
                                    border="2px solid black",
                                    _hover={
                                        "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                                    },
                                    width="100%",
                                ),
                                href=pysaas.State.get_lm_url,
                            ),
                            padding_top="2em",
                        ),
                        margin_bottom="1em",
                        style=styles.BOX_STYLES,
                        min_height="30em",
                        max_width="17em",
                    ),
                ),
                justify="center",
                spacing="1em",
            ),
        ),
        rx.mobile_only(
            rx.vstack(
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Pro",
                            font_size=styles.H3_FONT_SIZE,
                            font_weight=styles.BOLD_WEIGHT,
                            color="black",
                        ),
                        rx.text(
                            "Description of your Pro plan.",
                            color="#676767",
                        ),
                        rx.text(
                            rx.span(
                                rx.cond(
                                    pysaas.IndexState.yearly_pricing,
                                    pysaas.IndexState.pro_yr,
                                    pysaas.IndexState.pro_mo,
                                ),
                                font_size=styles.H2_FONT_SIZE,
                                font_weight=styles.BOLD_WEIGHT,
                                color="black",
                            ),
                            rx.cond(
                                pysaas.IndexState.yearly_pricing,
                                " / year",
                                " / month",
                            ),
                            font_size=styles.H4_FONT_SIZE,
                        ),
                        rx.list(
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            spacing="0.5em",
                            padding_top="0.5em",
                            color="#676767",
                        ),
                        rx.box(
                            rx.link(
                                rx.button(
                                    "Checkout",
                                    bg="black",
                                    box_shadow=styles.DOC_SHADOW_LIGHT,
                                    color="white",
                                    margin_top=0,
                                    size="md",
                                    border="2px solid black",
                                    _hover={
                                        "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                                    },
                                    width="100%",
                                ),
                                href=pysaas.State.get_lm_url,
                            ),
                            padding_top="2em",
                        ),
                        margin_bottom="1em",
                        style=styles.BOX_STYLES,
                        min_height="30em",
                    ),
                ),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Premium ",
                            rx.span(
                                rx.badge(
                                    "Most Popular", variant="subtle", color_scheme="green"
                                ),
                            ),
                            font_size=styles.H3_FONT_SIZE,
                            font_weight=styles.BOLD_WEIGHT,
                            color="black",
                        ),
                        rx.text(
                            "Description of your Premium plan.",
                            color="#676767",
                        ),
                        rx.text(
                            rx.span(
                                rx.cond(
                                    pysaas.IndexState.yearly_pricing,
                                    pysaas.IndexState.premium_yr,
                                    pysaas.IndexState.premium_mo,
                                ),
                                font_size=styles.H2_FONT_SIZE,
                                font_weight=styles.BOLD_WEIGHT,
                                color="black",
                            ),
                            rx.cond(
                                pysaas.IndexState.yearly_pricing,
                                " / year",
                                " / month",
                            ),
                            font_size=styles.H4_FONT_SIZE,
                        ),
                        rx.list(
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            spacing="0.5em",
                            padding_top="0.5em",
                            color="#676767",
                        ),
                        rx.box(
                            rx.link(
                                rx.button(
                                    "Checkout",
                                    bg="black",
                                    box_shadow=styles.DOC_SHADOW_LIGHT,
                                    color="white",
                                    margin_top=0,
                                    size="md",
                                    border="2px solid black",
                                    _hover={
                                        "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                                    },
                                    width="100%",
                                ),
                                href=pysaas.State.get_lm_url,
                            ),
                            padding_top="2em",
                        ),
                        margin_bottom="1em",
                        style=styles.POPULAR_PRICE_STYLES,
                        min_height="30em",
                    ),
                ),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Enterprise",
                            font_size=styles.H3_FONT_SIZE,
                            font_weight=styles.BOLD_WEIGHT,
                            color="black",
                        ),
                        rx.text(
                            "Description of your Enterprise plan.",
                            color="#676767",
                        ),
                        rx.text(
                            rx.span(
                                rx.cond(
                                    pysaas.IndexState.yearly_pricing,
                                    pysaas.IndexState.enterprise_yr,
                                    pysaas.IndexState.enterprise_mo,
                                ),
                                font_size=styles.H2_FONT_SIZE,
                                font_weight=styles.BOLD_WEIGHT,
                                color="black",
                            ),
                            rx.cond(
                                pysaas.IndexState.yearly_pricing,
                                " / year",
                                " / month",
                            ),
                            font_size=styles.H4_FONT_SIZE,
                        ),
                        rx.list(
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            rx.list_item(
                                rx.icon(tag="check_circle", color="green"),
                                " Allowed",
                            ),
                            spacing="0.5em",
                            padding_top="0.5em",
                            color="#676767",
                        ),
                        rx.box(
                            rx.link(
                                rx.button(
                                    "Checkout",
                                    bg="black",
                                    box_shadow=styles.DOC_SHADOW_LIGHT,
                                    color="white",
                                    margin_top=0,
                                    size="md",
                                    border="2px solid black",
                                    _hover={
                                        "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                                    },
                                    width="100%",
                                ),
                                href=pysaas.State.get_lm_url,
                            ),
                            padding_top="2em",
                        ),
                        margin_bottom="1em",
                        style=styles.BOX_STYLES,
                        min_height="30em",
                    ),
                ),
                justify="center",
                spacing="1em",
            ),
        ),
    ) 


def pricing() -> rx.Component:
    return rx.box(
        rx.tablet_and_desktop(
            rx.text(
                "Pricing",
                font_size="2em",
                font_weight=700,
            ),
            text_align="center",
            line_height="1.15",
            padding_bottom="0.5em",
        ),
        rx.mobile_only(
            rx.text(
                "Pricing",
                font_size="1.5em",
                font_weight=700,
            ),
            text_align="center",
            line_height="1.15",
            padding_bottom="0.5em",
        ),
        rx.container(
            "Fair pricing plans for every need.",
            color="grey",
            font_size="1.25em",
            text_align="center",
            padding_bottom="0.5em",
        ),
        pricing_cards(),
        width="70%",
        padding_top="10%",
        id="pricing",
    )


def cta() -> rx.Component:
    return rx.box(
        rx.box(
            rx.vstack(
                rx.heading(
                    "Start for free today.",
                    font_weight=styles.BOLD_WEIGHT,
                    font_size=styles.H3_FONT_SIZE,
                ),
                rx.cond(
                    pysaas.State.signed_out,
                    rx.link(
                        rx.button(
                            "Try it for free",
                            bg="white",
                            box_shadow=styles.DOC_SHADOW_LIGHT,
                            color="black",
                            margin_top=0,
                            size="sm",
                            border="2px solid white",
                            _hover={
                                "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                            },
                        ),
                        href="/signup",
                    ),
                    rx.link(
                        rx.button(
                            "Try it for free",
                            bg="white",
                            box_shadow=styles.DOC_SHADOW_LIGHT,
                            color="black",
                            margin_top=0,
                            size="sm",
                            border="2px solid white",
                            _hover={
                                "box_shadow": "0 0 .12em .07em #6495ED, 0 0 .25em .11em #6495ED",
                            },
                        ),
                        href="/dashboard",
                    ),
                ),
                align_items="center",
                justify="center",
                max_width="38em",
                margin_x="auto",
                spacing="1em",
            ),
            padding_x=styles.PADDING_X2,
            font_size="1.2em",
            padding_y="4em",
            color="white",
            bg="black",
        ),
        padding_top="10%",
        width="100%",
    )