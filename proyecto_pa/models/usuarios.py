import reflex as rx
import bcrypt
from sqlmodel import Field

class usuarios(rx.Model, table=True):

    #Va controlar el como se ve la tabla  en la db
    id: int = Field(default=None, primary_key=True)
    nombre: str
    email: str
    password: str

    @classmethod
    def crear_usuario(cls,nombre_usuario, correo_usuario, pass_usuario):
        #vamos a pasar la contraseña por un proceso de hasheo
        #genera la contraseña pero en byte
       
        pass_codificada = pass_usuario.encode()

        #esto hashea la contraseña y la regresa en bytes
        pass_hasheada = bcrypt.hashpw(pass_codificada, bcrypt.gensalt())
     
        #                                                                 con el decode convertimos de bytes a str
        return cls(nombre=nombre_usuario, email=correo_usuario, password=pass_hasheada.decode())