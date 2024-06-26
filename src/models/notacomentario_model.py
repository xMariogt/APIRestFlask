from sqlalchemy import ForeignKey, Integer
from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column


class NotaComentarioModel(db.Model):
    __tablename__ = "NOTA_COMENTARIO"
    IDNOTA:Mapped [int] = mapped_column(Integer, ForeignKey('NOTA.IDNOTA'), primary_key=True)
    IDCOMENTARIO:Mapped [int] = mapped_column(Integer, ForeignKey('COMENTARIO.IDCOMENTARIO'), primary_key=True)    
