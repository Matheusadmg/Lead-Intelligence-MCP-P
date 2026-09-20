from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from .historico_interacoes_model import HistoricoInteracoesModel

class LeadsModel(Base):
    __tablename__ = 'leads'

    id_pessoa: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    email: Mapped[str] = mapped_column(String(255))
    nome: Mapped[str] = mapped_column(String(50))
    cargo: Mapped[str | None] = mapped_column(String(50))
    empresa: Mapped[str | None] = mapped_column(String(50))
    setor: Mapped[str | None] = mapped_column(String(50))
    score_atual: Mapped[int] = mapped_column(Integer)
    cenario_teste: Mapped[str] = mapped_column(String(255))
    resultado_analise_ia: Mapped[str | None] = mapped_column(String(255))
    historico: Mapped[list["HistoricoInteracoesModel"]] = relationship(
        cascade="all, delete-orphan",
        lazy="selectin"
    )

