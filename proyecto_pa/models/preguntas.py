#todo lo relacionado ala preguntas y su tabla

import reflex as rx
from sqlmodel import Field, Relationship, SQLModel

from ..Auth import AuthState

LLAVE_SECRETA = "6hL6xD9OkIF9O2GhjP7x"



class Preguntas(rx.Model, table=True):
    id: int= Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key='usuarios.id', nullable=False)
    pregunta: str
    detalles: str

    #crearemos un metodo que me permita ingresar las prguntas directamente en la db
    @classmethod
    def crear_pregunta(cls, id_usuario, pregunta, detalles):
        return cls(usuario_id=id_usuario, pregunta=pregunta, detalles=detalles)
    


