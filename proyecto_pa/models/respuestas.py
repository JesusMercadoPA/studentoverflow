from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime

class Respuestas(SQLModel, table=True):
    __tablename__ = "respuestas"

    id: Optional[int] = Field(default=None, primary_key=True)
    pregunta_id: int = Field(foreign_key="preguntas.id")  # Relación con Preguntas
    usuario_id: int = Field(foreign_key="usuarios.id")    # Relación con Usuarios
    texto: str
    fecha_creacion: datetime = Field(default_factory=datetime.utcnow)
