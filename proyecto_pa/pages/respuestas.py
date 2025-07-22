import reflex as rx
from ..Auth import AuthState

@rx.page(route="/respuestas", title="Gracias por tu pregunta")
def pagina_respuestas() -> rx.Component:
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

        # Contenedor centrado
        rx.center(
            rx.box(
                rx.vstack(
                    rx.badge(
                        rx.icon(tag="check_circle", size=32),
                        color_scheme="green",
                        radius="full",
                        padding="0.65rem",
                    ),
                    rx.heading(
                        "¡Pregunta enviada con éxito!", 
                        size="4",
                        weight="bold",
                        color="green",
                    ),
                    rx.text(
                        "Gracias por compartir tu pregunta con la comunidad. "
                        "Pronto recibirás una respuesta.",
                        size="2",
                        text_align="center",
                        line_height="35px",
                        max_width="500px",
                    ),
                    # Botón para volver a preguntas
                    rx.button(
                        "Volver a Preguntas",
                        on_click=lambda: rx.redirect("/questionComponent"),
                        color_scheme="blue",
                        margin_top="2rem",
                        width="100%",
                        size="2",
                    ),
                    # Botón para ir a ver respuestas de la comunidad
                    rx.button(
                        "Ver Respuestas de la Comunidad",
                        on_click=lambda: rx.redirect("/respuestas_comunidad"),
                        color_scheme="teal",
                        margin_top="1rem",
                        width="100%",
                        size="2",
                    ),
                    spacing="5",
                    align_items="center",
                    width="100%",
                ),
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
