from typing import List
from src.models.nota_model import NotaModel
from src.models.comentario_model import ComentarioModel
from src.common.utils import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class UsuarioModel(db.Model):
    __tablename__ = "USUARIO"
    IDUSUARIO:Mapped[int] = mapped_column(primary_key=True)
    NOMBRE:Mapped[str] = mapped_column(nullable=False)
    CORREO:Mapped[str] = mapped_column(nullable=False)
    CONTRASENIA:Mapped[str] = mapped_column(nullable=False)
    
    #relationships
    COMENTARIOS: Mapped[List[ComentarioModel]] = relationship(back_populates="USUARIO")
    NOTAS: Mapped[List[NotaModel]] = relationship()