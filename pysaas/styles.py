'''

styles.py

This file contains:
    1. The app styles used within page components.

'''


import reflex as rx


BOLD_WEIGHT = "800"
NAVBAR_LOGO = "/navbar_logo.png"
SITE_GRADIENT = {
    'background_image': "linear-gradient(371.68deg, #7F00FF 25%, #6495ED 50%)",
}
HEADING_COLOR_GRADIENT = {
    'background_image': "linear-gradient(371.68deg, #7F00FF 25%, #6495ED 50%)",
    'background_clip': "text",
}
RANDOM_GRADIENT = [
    {
        'background_image': "linear-gradient(43.5deg, #6495ED 25%, #7F00FF 50%)",
        'background_clip': "text",
    },
    {
        'background_image': "linear-gradient(114.44deg, #7F00FF 25%, #6495ED 50%)",
        'background_clip': "text",
    },
    {
        'background_image': "linear-gradient(205.32deg, #6495ED 25%, #7F00FF 50%)",
        'background_clip': "text",
    },
]
LOGO_URL = "/logo.svg"
PADDING_X = ["1em", "2em", "5em"]
PADDING_X2 = ["1em", "2em", "10em"]
HERO_FONT_SIZE = ["2em", "3em", "3em", "4em"]
H1_FONT_SIZE = ["2.2em", "2.4em", "2.5em"]
H2_FONT_SIZE = ["1.8em", "1.9em", "2em"]
H3_FONT_SIZE = "1.35em"
H4_FONT_SIZE = "1.1em"
TEXT_FONT_SIZE = "1em"
TEXT_FONT_FAMILY = "Inter"
CODE_FONT_FAMILY = "Fira Code, Fira Mono, Menlo, Consolas, DejaVu Sans Mono, monospace"
ACCENT_COLOR = "#6495ED"
ACCENT_COLOR_LIGHT = "rgba(107,99,246, 0.4)"
ACCENT_COLOR_DARK = "rgb(86, 77, 209)"
SUBHEADING_COLOR = "rgb(37,50,56)"
LIGHT_TEXT_COLOR = "#94a3b8"
LINK_STYLE = {
    "color": ACCENT_COLOR,
    "text_decoration": "underline",
}


DOC_HEADER_COLOR = "#000000"
DOC_TEXT_COLOR = "#000000"
DOC_REG_TEXT_COLOR = "#666666"
DOC_LIGHT_TEXT_COLOR = "#999999"
DOCPAGE_BACKGROUND_COLOR = "#fafafa"

DOC_HEADING_FONT_WEIGHT = "900"
DOC_SUBHEADING_FONT_WEIGHT = "800"
DOC_SECTION_FONT_WEIGHT = "600"

DOC_SHADOW = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
DOC_SHADOW_DARK = "rgba(0, 0, 0, 0.3) 0px 2px 8px"
DOC_SHADOW_LIGHT = "rgba(0, 0, 0, 0.08) 0px 4px 12px"

DOC_BORDER_RADIUS = "1em"


BASE_STYLE = {
    "::selection": {
        "background_color": ACCENT_COLOR_LIGHT,
    },
    'a': {
        'text_decoration': 'underline',
        'text_color': 'grey',
    },
    'li': {
        'padding_left': '2em',
    },
    rx.Divider: {"margin_bottom": "1em", "margin_top": "0.5em"},
    rx.Code: {
        "color": ACCENT_COLOR,
    },
}


STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap",
    "https://fonts.googleapis.com/css2?family=Silkscreen&display=swap",
]


LOGO_NAV_STYLE = {
    "width": "1.605em",
    "height": "1.5em",
}

LOGO_FOOTER_STYLE = {
    "width": ["2.568em", "2.568em", "3.21em"],
    "height": ["2.4em", "2.4em", "3em"],
}

BUTTON_STYLE = {
    "color": DOC_REG_TEXT_COLOR,
    "_hover": {"color": ACCENT_COLOR, "text_decoration": "none"},
}

FOOTER_ITEM_STYLE = {
    "font_weight": "500",
    "_hover": {"color": ACCENT_COLOR},
}

BOX_STYLES = {
    "background": "white",
    "border": "1px solid #e5e5e5",
    "border_radius": "1em",
    "padding": "1em",
    "box_shadow": """
    rgba(17, 7, 53, 0.05) 0px 51px 78px 0px, rgba(17, 7, 53, 0.035) 0px 21.3066px 35.4944px 0px, rgba(17, 7, 53, 0.03) 0px 11.3915px 18.9418px 0px, rgba(17, 7, 53, 0.024) 0px 6.38599px 9.8801px 0px, rgba(17, 7, 53, 0.02) 0px 3.39155px 4.58665px 0px, rgba(17, 7, 53, 0.016) 0px 1.4113px 1.55262px 0px, rgba(41, 56, 78, 0.05) 0px 1px 0px 0px inset
    """,
    "height": "100%",
    "align_items": "left",
    "width": "100%",
    "min_height": "15em",
    "padding": "2em",
    "bg": "rgba(248, 248, 248, .75)",
    "_hover": {
        "box_shadow": """
        rgba(23, 6, 100, 0.035) 0px 24px 22px 0px, rgba(23, 6, 100, 0.055) 0px 8.5846px 8.03036px 0px, rgba(23, 6, 100, 0.067) 0px 4.77692px 3.89859px 0px, rgba(23, 6, 100, 0.082) 0px 2.63479px 1.91116px 0px, rgba(23, 6, 100, 0.12) 0px 1.15891px 0.755676px 0px
        """,
    },
}

DASH_STYLES = {
    "background": "white",
    "border": "1px solid #e5e5e5",
    "border_radius": "1em",
    "height": "100%",
    "align_items": "left",
    "width": "100%",
    "min_height": "2em",
    "padding": "1.2em",
}

POPULAR_PRICE_STYLES = {
    "border": "3.5px solid black",
    "border_radius": "1em",
    "box_shadow": """
    rgba(17, 7, 53, 0.05) 0px 51px 78px 0px, rgba(17, 7, 53, 0.035) 0px 21.3066px 35.4944px 0px, rgba(17, 7, 53, 0.03) 0px 11.3915px 18.9418px 0px, rgba(17, 7, 53, 0.024) 0px 6.38599px 9.8801px 0px, rgba(17, 7, 53, 0.02) 0px 3.39155px 4.58665px 0px, rgba(17, 7, 53, 0.016) 0px 1.4113px 1.55262px 0px, rgba(41, 56, 78, 0.05) 0px 1px 0px 0px inset
    """,
    "height": "100%",
    "align_items": "left",
    "width": "100%",
    "min_height": "15em",
    "padding": "2em",
    "bg": "rgba(248, 248, 248, .75)",
    "_hover": {
        "box_shadow": """
        rgba(23, 6, 100, 0.035) 0px 24px 22px 0px, rgba(23, 6, 100, 0.055) 0px 8.5846px 8.03036px 0px, rgba(23, 6, 100, 0.067) 0px 4.77692px 3.89859px 0px, rgba(23, 6, 100, 0.082) 0px 2.63479px 1.91116px 0px, rgba(23, 6, 100, 0.12) 0px 1.15891px 0.755676px 0px
        """,
    },
}

SIGNIN_PAGE_STYLES = {
    "padding_top": "5em",
    "text_align": "top",
    "position": "relative",
    "background": DOCPAGE_BACKGROUND_COLOR,
    "background_size": "100% auto",
    "width": "100%",
    "height": "100vh",
}

SIGNIN_INPUT_STYLES = {
    "border_radius": "1em",
    "padding": "1em",
    "box_shadow": """
    rgba(17, 7, 53, 0.05) 0px 51px 78px 0px, rgba(17, 7, 53, 0.035) 0px 21.3066px 35.4944px 0px, rgba(17, 7, 53, 0.03) 0px 11.3915px 18.9418px 0px, rgba(17, 7, 53, 0.024) 0px 6.38599px 9.8801px 0px, rgba(17, 7, 53, 0.02) 0px 3.39155px 4.58665px 0px, rgba(17, 7, 53, 0.016) 0px 1.4113px 1.55262px 0px, rgba(41, 56, 78, 0.05) 0px 1px 0px 0px inset
    """,
    "background": "white",
}