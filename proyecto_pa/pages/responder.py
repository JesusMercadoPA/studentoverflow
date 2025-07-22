import reflex as rx
from ..models.respuestas import Respuestas
from ..models.preguntas import Preguntas
from ..Auth import AuthState

class EstadoRespuesta(rx.State):
    texto: str = ""

    @rx.event
    def enviar_respuesta(self, form_data: dict):
        """Guarda una nueva respuesta en la base de datos."""
        self.texto = form_data["texto"]

        id_usuario = 15  # Aquí deberías obtener el usuario logueado
        pregunta_id = 2  # Por ahora lo dejamos fijo, luego podemos pasarlo como parámetro

        nueva_respuesta = Respuestas(
            pregunta_id=pregunta_id,
            usuario_id=id_usuario,
            texto=self.texto,
        )

        with rx.session() as sesion:
            sesion.add(nueva_respuesta)
            sesion.commit()

        return rx.redirect("/respuestas_comunidad")

def componente_respuesta() -> rx.Component:
    """Formulario para responder."""
    return rx.card(
        rx.vstack(
            rx.heading("Responde a la pregunta", size="4", weight="bold"),
            rx.form.root(
                rx.text_area(
                    placeholder="Escribe tu respuesta...",
                    name="texto",
                    resize="vertical",
                ),
                rx.form.submit(
                    rx.button("Enviar respuesta", color_scheme="blue"),
                    as_child=True,
                ),
                on_submit=EstadoRespuesta.enviar_respuesta,
                reset_on_submit=True,
            ),
            spacing="4",
        ),
        size="3",
        padding="2rem",
    )

@rx.page(route="/responder", title="Responder pregunta")
def pagina_responder() -> rx.Component:
    return rx.box(
        # Botón cerrar sesión fijo arriba
        rx.button(
            "Cerrar sesión",
            on_click=AuthState.cerrar_sesion,
            position="fixed",
            top="1rem",
            right="1rem",
            variant="outline",
            border_color="white",
            color="white",
        ),
        rx.center(
            rx.box(
                componente_respuesta(),
                max_width="600px",
                width="100%",
                padding="2rem",
                bg="white",
                border_radius="lg",
                box_shadow="lg",
            ),
            height="100vh",
            padding="2rem",
        ),
        height="100vh",
        bg="#3e87f3",
        position="relative",
    )
