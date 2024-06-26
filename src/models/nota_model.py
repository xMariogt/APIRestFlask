from typing import List
from src.common.utils import db
from sqlalchemy import Integer, String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.notacomentario_model import NotaComentarioModel
import datetime

class NotaModel(db.Model):
    __tablename__ = "NOTA"
    #campos
    IDNOTA: Mapped[int] = mapped_column(primary_key=True)
    DESCRIPCION: Mapped[str] = mapped_column(nullable=False)
    FECHA: Mapped[datetime.datetime] = mapped_column(nullable=False)
    IDUSUARIO: Mapped[int] = mapped_column(Integer, ForeignKey("USUARIO.IDUSUARIO"), nullable=False)
    
    #relaciones
    COMENTARIOS: Mapped[List["ComentarioModel"]] = relationship(secondary="NOTA_COMENTARIO")