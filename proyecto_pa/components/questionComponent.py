import reflex as rx
from ..models.preguntas import Preguntas
from ..Auth import AuthState

class EstadoPregunta(rx.State):
    pregunta: str = ""
    detalles: str = ""

    @rx.event
    def obtener_pregunta(self, form_data: dict):
        id_usuario = 15  # Puedes cambiarlo según el usuario autenticado
        self.pregunta = form_data['pregunta']
        self.detalles = form_data['detalles']

        nueva_pregunta = Preguntas.crear_pregunta(
            id_usuario=id_usuario,
            pregunta=self.pregunta,
            detalles=self.detalles
        )
        with rx.session() as sesion:
            sesion.add(nueva_pregunta)
            sesion.commit()
        return rx.redirect("/respuestas")  # Cambia la ruta si quieres

def form_field(label: str, placeholder: str, type: str, name: str) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input(
                    placeholder=placeholder,
                    type=type,
                ),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width="100%",
    )

def componente_pregunta() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="message_circle_question", size=32),
                    color_scheme="blue",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.heading(
                        "¿Tienes preguntas?",
                        size="4",
                        weight="bold",
                    ),
                    rx.text(
                        "Compártelas con la comunidad",
                        size="2",
                    ),
                    spacing="1",
                    height="100%",
                ),
                height="100%",
                spacing="4",
                align_items="center",
                width="100%",
            ),
            rx.form.root(
                rx.flex(
                    rx.flex(
                        form_field(
                            "¿Cuál es tu pregunta?",
                            "Ingresa tu pregunta",
                            "text",
                            "pregunta",
                        ),
                        flex_direction=["column", "row", "row"],
                    ),
                    rx.flex(
                        rx.text(
                            "Detalles",
                            style={
                                "font-size": "15px",
                                "font-weight": "500",
                                "line-height": "35px",
                            },
                        ),
                        rx.text_area(
                            placeholder="Pon más detalles de la pregunta...",
                            name="detalles",
                            resize="vertical",
                        ),
                        direction="column",
                        spacing="1",
                    ),
                    rx.form.submit(
                        rx.button("Enviar", color_scheme="blue"),
                        as_child=True,
                    ),
                    direction="column",
                    spacing="2",
                    width="100%",
                ),
                on_submit=EstadoPregunta.obtener_pregunta,
                reset_on_submit=False,
            ),
            width="100%",
            direction="column",
            spacing="4",
        ),
        size="3",
    )

@rx.page(route="/questionComponent", title="Haz una pregunta")
def pagina_pregunta() -> rx.Component:
    return rx.box(
        # Botón cerrar sesión fijo arriba a la derecha
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

        # Contenedor centrado para el formulario
        rx.center(
            rx.box(
                componente_pregunta(),
                max_width="600px",
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
