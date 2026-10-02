from datetime import datetime
from dataclasses import dataclass


@dataclass
class HistoricoInteracoesEntity:
    id: int
    id_pessoa: int
    acao: str
    item: str
    data: datetime

