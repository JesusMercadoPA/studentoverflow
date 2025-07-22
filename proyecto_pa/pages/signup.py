import reflex as rx

from ..models.usuarios import usuarios
from sqlmodel import select
from ..Auth import AuthState

class EstadoSignup(rx.State):

    email: str = ""
    password: str = ""
    nombre: str = ""

    @rx.event
    def asignarCorreo(self, correo_ingresado):
        self.email = correo_ingresado

    @rx.event
    def asignarPassword(self, pass_ingresada):
        self.password = pass_ingresada

    @rx.event
    def asignarNombre(self, nombre_ingresado):
        self.nombre = nombre_ingresado

    
    def buscar_usuario(self):
        
        with rx.session() as sesion:

            usuario_registrado = sesion.exec(
                select(usuarios).where(usuarios.email == self.email)
            ).first()

        
        return usuario_registrado

    @rx.event
    def registar_cuenta(self):

        usuario_registrado = self.buscar_usuario()
        
        if usuario_registrado:
            print("El usuario ya esta registrado")
            self.email = ""
            
                     
        else:
          
          nuevo_usuario = usuarios.crear_usuario(
            self.nombre,
            self.email,
            self.password
            )

          with rx.session() as sesion:

            sesion.add(nuevo_usuario)

            sesion.commit()

         
          return rx.redirect("/login")   

    @rx.event
    def mostrar_info(self):
        print(self.nombre)
        print(self.email)
        print(self.password) 
        
@rx.page(
        route="/signup",
        on_load=AuthState.verificar_usuario
)


def pagina_signup() ->rx.Component:
    return rx.box(
        rx.center(
            rx.box(
                rx.vstack(
                    rx.heading("Regístrate"),
                    rx.input(
                        placeholder="Nombre",
                        type="text",
                        value=EstadoSignup.nombre,
                        on_change=EstadoSignup.asignarNombre,
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Correo",
                        type="email",
                        value=EstadoSignup.email,
                        on_change=EstadoSignup.asignarCorreo,
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Contraseña",
                        type="password",
                        value=EstadoSignup.password,
                        on_change=EstadoSignup.asignarPassword,
                        width="100%",
                    ),
                    rx.button(
                        "Crear una cuenta",
                        on_click=EstadoSignup.registar_cuenta,
                        color_scheme="blue",
                        width="100%",
                        
                        # Fondo azul sólido, texto blanco por defecto
                    ),
                    rx.button(
                        "Iniciar sesión",
                        on_click=lambda: rx.redirect("/login"),
                        color_scheme="blue",
                        width="100%",
                        variant="outline",  # Botón blanco con borde y texto azul
                    ),
                ),
                max_width="400px",
                width="100%",
                padding="2rem",
                bg="white",
                border_radius="lg",
                box_shadow="md",
                spacing="4",
            ),
            height="100vh",
            padding="2rem",
        ),
        bg="#3e87f3",
        height="100vh",
        width="100%",
)