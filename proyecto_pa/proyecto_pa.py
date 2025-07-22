"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .pages.info import pagina_info
from .pages.login import pagina_login
from .pages.signup import pagina_signup
from .pages.dashboard import pagina_dashboard
from .Auth import AuthState
from .pages.respuestas import pagina_respuestas
from .pages.respuestasComunidad import pagina_respuestas_comunidad
from .pages.responder import pagina_responder



def index() -> rx.Component:
     # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("¡Bienvenido mi web de app!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            
            rx.link(
                rx.button("Da click para inciar"),
                href="http://localhost:3000/login/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )

app = rx.App()
app.add_page(index)
app.add_page(pagina_info)
app.add_page(pagina_login, route="/login", title="Iniciar sesion")
app.add_page(pagina_signup, route="/singup", title="Registro")
app.add_page(pagina_dashboard, route="/dashboard", title="Dashboard")
app.add_page(pagina_respuestas, route="/respuestas", title="Gracias")
app.add_page(pagina_respuestas_comunidad, route="/respuestas_comunidad", title="Respuestas de la Comunidad")
app.add_page(pagina_responder, route="/responder", title="Responder pregunta")






#Gusbunbury1707. contraseña de supabase para la base de datos