from datetime import date
from dataclasses import dataclass


@dataclass
class HistoricoInteracoesEntity:
    id: int
    id_pessoa: int
    acao: str
    item: str
    data: date

