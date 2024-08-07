"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from Postin_Frontend.auth import signup_default, login_default, navbar_user


class State(rx.State):
    """The app state."""

    ...

@rx.page(route="/home", title="Home Page")
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="bottom-left"),
        rx.button("Logout", size="3", width="20%", on_click=rx.redirect("/")),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        panel_background="solid",
        scaling="90%",
        radius="medium",
        accent_color="crimson"
    )
)
app.add_page(navbar_user)
app.add_page(login_default)
app.add_page(signup_default)
app.add_page(index)
