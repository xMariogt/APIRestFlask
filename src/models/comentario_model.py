import datetime
from sqlalchemy import Integer
from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column, relationship

class ComentarioModel(db.Model):
    __tablename__ = "COMENTARIO"
    IDCOMENTARIO: Mapped[int] = mapped_column(primary_key=True)
    DESCRIPCION: Mapped[str] = mapped_column(nullable=False)
    FECHA: Mapped[datetime.datetime] = mapped_column(nullable=False)
    IDUSUARIO: Mapped[int] = mapped_column(Integer, db.ForeignKey("USUARIO.IDUSUARIO"), nullable=False)
    
    #relationships
    USUARIO: Mapped["UsuarioModel"] = relationship(back_populates="COMENTARIOS")