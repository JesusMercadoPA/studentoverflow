import reflex as rx
from ..models.usuarios import usuarios
from sqlmodel import select
import bcrypt
from ..Auth import AuthState

import datetime
import jwt  
LLAVE_SECRETA = "6hL6xD9OkIF9O2GhjP7x"

class EstadoLogin(rx.State):

    email: str = ""
    password: str = "" 
    cargando: bool = False
    error: bool = False
    

    @rx.event
    def asignarCorreo(self, correo_ingresado):
        self.email = correo_ingresado

    @rx.event
    def asignarPassword(self, pass_ingresada):
        self.password = pass_ingresada


    def buscar_usuario(self):
        
        with rx.session() as sesion:

            usuario_registrado = sesion.exec(
                select(usuarios).where(usuarios.email == self.email)
            ).first()

        
        return usuario_registrado
    
    def verificar_password(self, password_db):
        return bcrypt.checkpw(self.password.encode(), password_db.encode())

    @rx.event
    def iniciar_sesion(self):
        self.cargando = True
        self.error = False
        yield # si ponemos un yield sin nada en regresar la ui se actuliza

        usuario = self.buscar_usuario()
        
        if usuario and self.verificar_password(usuario.password):
            print("Inicio de sesion exitoso")
       

            datos_token = {
                "user_id": usuario.id,
                "user_name": usuario.nombre,
                "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=20)
            }


            token = jwt.encode(datos_token, LLAVE_SECRETA, algorithm="HS256")

            yield AuthState.guardar_token(token)
            self.cargando = False
            
            return rx.redirect("/questionComponent")  

        else:
            print("Correo o contraseña incorrecto")
            self.error = True
            self.password = ""
            self.cargando = False
            yield
            
            

    @rx.event
    def mostrar_info(self):
       
        print(self.email)
        print(self.password) 
        print("------------")  
        if self.email == "admin@correo.com" and self.password == "123":
            print(f"Bienvenido {self.nombre} (Admin)")
          
            self.email = ""
            self.password = ""
        else:
            print("correo o contraseña incorrecta")
             
            self.email = ""
            self.password = ""

@rx.page(
        route="/login",
        on_load=AuthState.verificar_usuario
         )
def pagina_login() -> rx.Component:
        return rx.box(
        rx.center(
            rx.box(
                rx.vstack(
                    rx.heading("Inicio de sesión", size="6"),

                    rx.input(
                        placeholder="correo",
                        type="email",
                        value=EstadoLogin.email,
                        on_change=EstadoLogin.asignarCorreo,
                        align="center",
                        width="100%"
                    ),
                    rx.input(
                        placeholder="contraseña",
                        type="password",
                        value=EstadoLogin.password,
                        on_change=EstadoLogin.asignarPassword,
                        align="center",
                        width="100%"
                    ),
                    rx.cond(
                        EstadoLogin.cargando,
                        rx.button(
                            rx.spinner(loading=True),
                            "iniciar sesión",
                            color_scheme="red",
                            disabled=True,
                            align="center",
                            width="100%"
                        ),
                        rx.button(
                            "iniciar sesión",
                            on_click=EstadoLogin.iniciar_sesion,
                            color_scheme="blue",
                            align="center",
                            width="100%"
                        ),
                    ),
                    # BOTÓN DE REGISTRO
                    rx.button(
                        "¿No tienes cuenta? Regístrate",
                        on_click=lambda: rx.redirect("/signup"),
                        color_scheme="blue",
                        variant="outline",
                        width="100%",
                        margin_top="10px"
                    ),
                    rx.box(
                        rx.cond(
                            EstadoLogin.error,
                            rx.callout(
                                "El usuario y/o contraseña es incorrecto",
                                icon="triangle_alert",
                                color_scheme="red",
                                role="alert"
                            ),
                        )
                    )
                ),
                max_width="400px",
                width="100%",
                padding="2rem",
                bg="white",
                border_radius="lg",
                box_shadow="md",
            ),
            height="100vh",
            padding="2rem",
        ),
        bg="#3e87f3",
        height="100vh",
        width="100%",
    )

   #  rx.spinner(
                    #     size="3",
                 
                 #        align="center",
                 #   3    justify="center"
              #     ),