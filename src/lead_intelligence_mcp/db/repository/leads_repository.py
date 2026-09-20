from sqlalchemy.ext.asyncio import AsyncSession
from .base import BaseRepository
from ..models.leads_model import LeadsModel

class LeadRepository(BaseRepository[LeadsModel]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session=session, model=LeadsModel)