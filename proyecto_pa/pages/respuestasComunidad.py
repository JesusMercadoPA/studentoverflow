import reflex as rx
from ..models.respuestas import Respuestas
from ..Auth import AuthState


class EstadoRespuestas(rx.State):
    lista_respuestas: list[dict] = []

    @rx.event
    def cargar_respuestas(self):
        with rx.session() as sesion:
            respuestas = sesion.query(Respuestas).all()
            self.lista_respuestas = [
                {
                    "id": r.id,
                    "texto": r.texto,           # CAMBIO
                    "usuario_id": r.usuario_id  # CAMBIO
                }
                for r in respuestas
            ]


def listado_respuestas() -> rx.Component:
    return rx.box(
        rx.foreach(
            EstadoRespuestas.lista_respuestas,
            lambda r: rx.card(
                rx.vstack(
                    rx.heading(f"Respuesta de Usuario {r['usuario_id']}", size="3"),
                    rx.text(r["texto"], size="2", color="gray"),  # CAMBIO
                ),
                size="3",
                margin_bottom="1rem",
                width="100%",
            ),
        )
    )


@rx.page(
    route="/respuestas_comunidad",
    title="Respuestas de la Comunidad",
    on_load=EstadoRespuestas.cargar_respuestas,
)
def pagina_respuestas_comunidad() -> rx.Component:
    return rx.box(
        # Botón cerrar sesión arriba a la derecha
        rx.button(
            "Cerrar sesión",
            on_click=AuthState.cerrar_sesion,
            position="fixed",
            top="1rem",
            right="1rem",
            z_index="1000",
            variant="outline",
            border_color="white",
            color="white",
            _hover={"bg": "rgba(255, 255, 255, 0.1)"},
        ),

        # Contenedor principal
        rx.center(
            rx.box(
                rx.vstack(
                    rx.heading("Respuestas de la Comunidad", size="4", weight="bold"),
                    listado_respuestas(),
                    spacing="5",
                    width="100%",
                ),
                max_width="700px",
                width="100%",
                padding="2rem",
                bg="white",
                box_shadow="lg",
                border_radius="lg",
            ),
            height="100vh",
            padding="2rem",
        ),
        height="100vh",
        bg="#3e87f3",
        position="relative",
    )
