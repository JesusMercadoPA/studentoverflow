import reflex as rx
from ..Auth import AuthState
from ..components.questionComponent import componente_pregunta  # Importa el componente correcto

@rx.page(
    route="/dashboard",
    on_load=AuthState.verificar_token
)
def pagina_dashboard() -> rx.Component:
    return rx.container(
        rx.cond(
            AuthState.esta_cargando,
            rx.center(
                rx.text("cargando...", align="center"),
            ),
            rx.container(
                rx.center(
                    rx.vstack(
                        rx.heading("Bienvenido", size="6", align="center", width="100%"),
                        rx.button(
                            "cerrar sesion",
                            on_click=AuthState.cerrar_sesion,
                            color_scheme="blue",
                            margin_left="5x",
                            justify="center",
                            width="100%",
                        ),
                        rx.divider(),
                        componente_pregunta(),  # Aquí llamas al componente correcto
                    )
                )
            )
        )
    )
