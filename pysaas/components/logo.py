import reflex as rx

import pysaas.styles as styles


def logo(**style_props):
    """Create a Pynecone logo component.
    Args:
        style_props: The style properties to apply to the component.
    """
    return rx.image(
        src=styles.LOGO_URL,
        **style_props,
    )