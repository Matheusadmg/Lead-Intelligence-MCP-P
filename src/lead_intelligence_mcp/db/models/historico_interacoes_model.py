from sqlalchemy import ForeignKey, String, Date
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class HistoricoInteracoesModel(Base):
    __tablename__ = 'historico_interacoes'

    id: Mapped[int] = mapped_column(primary_key=True)
    id_pessoa: Mapped[int] = mapped_column(ForeignKey('leads.id_pessoa'))
    acao: Mapped[str] = mapped_column(String(50))
    item: Mapped[str] = mapped_column(String(50))
    data: Mapped[str] = mapped_column(String(10))

