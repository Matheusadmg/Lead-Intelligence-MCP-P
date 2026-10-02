from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .base import BaseRepository
from ..models.historico_interacoes_model import HistoricoInteracoesModel
from ..session import get_db_session


class HistoricoInteracoesRepository(BaseRepository[HistoricoInteracoesModel]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session=session, model=HistoricoInteracoesModel)

def get_historico_repository(session: AsyncSession = Depends(get_db_session)) -> (
        HistoricoInteracoesRepository):
    return HistoricoInteracoesRepository(session)