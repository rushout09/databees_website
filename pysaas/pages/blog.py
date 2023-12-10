import reflex as rx

from pysaas.components.navbar import navbar
from pysaas.components.post import posts, post_details
from pysaas.components.footer import blog_footer


def blog() -> rx.Component:
    return rx.center(
        rx.vstack(
            navbar(),
            posts(),
            blog_footer(),
            width="100%",
        ),
    )


def post() -> rx.Component:
    return rx.center(
        rx.vstack(
            navbar(),
            post_details(),
            blog_footer(),
            width="100%",
        ),
    )