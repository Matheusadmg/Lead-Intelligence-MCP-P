from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .base import BaseRepository
from ..models.lead_model import LeadModel
from ..session import get_db_session


class LeadRepository(BaseRepository[LeadModel]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session=session, model=LeadModel)

def get_lead_repository(session: AsyncSession = Depends(get_db_session)) -> (
        LeadRepository):
    return LeadRepository(session)