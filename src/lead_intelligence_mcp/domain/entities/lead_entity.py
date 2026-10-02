from pydantic import BaseModel, EmailStr, Field
from .historico_interacoes_entity import HistoricoInteracoesEntity

class LeadEntity(BaseModel):
    id: int
    nome: str = Field(pattern=r"^[a-zA-Z]+(?: [a-zA-Z]+)*$")
    email: EmailStr
    cargo: str | None
    empresa: str | None
    setor: str | None
    score_atual: float
    resultado_analise_ia: str | None
    historico: list[HistoricoInteracoesEntity] = Field(default_factory=list)