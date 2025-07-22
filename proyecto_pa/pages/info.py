import reflex as rx

class ContadorEstado(rx.State):
    contador:int = 0

    @rx.event
    def incrementar_contador(self):
        self.contador += 1

    @rx.event
    def decrementar_contador(self):
        self.contador -= 1

@rx.page(route="/informacion", title="About us")
def pagina_info() -> rx.Component:
    
    #creamos un contenedor de espacio de trabajo 
    return rx.container(
       rx.center( 
           rx.vstack(
                rx.text("Cambio de estado", size="4"),
                rx.text(ContadorEstado.contador, size="9", justify="center"),
                rx.button(
                    "Incrementar",
                    on_click=ContadorEstado.incrementar_contador,
                ),
                rx.button(
                    "Decrementar",
                    on_click=ContadorEstado.decrementar_contador 
                )
            )
        )
    ) 
