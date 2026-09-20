from sqlalchemy.ext.asyncio import AsyncSession
from .base import BaseRepository
from ..models.historico_interacoes_model import HistoricoInteracoesModel

class HistoricoInteracoesRepository(BaseRepository[HistoricoInteracoesModel]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session=session, model=HistoricoInteracoesModel)