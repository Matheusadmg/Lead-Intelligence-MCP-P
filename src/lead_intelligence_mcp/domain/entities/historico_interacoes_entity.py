from datetime import date
from pydantic import BaseModel

class HistoricoInteracoesEntity(BaseModel):
    id: int
    id_pessoa: int
    acao: str
    item: str
    data: date

