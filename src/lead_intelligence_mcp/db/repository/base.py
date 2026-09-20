from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import TypeVar, Generic, Sequence, Any
from sqlalchemy.orm import DeclarativeBase

T = TypeVar("T", bound=DeclarativeBase)

class BaseRepository(Generic[T]):
    def __init__(self, session: AsyncSession, model: type[T]) -> None:
        self.session = session
        self.model = model

    async def get_by_id(self, id: int) -> T | None:
        return await self.session.get(self.model, id)

    async def get_all(self) -> Sequence[T] | None:
        query = select(self.model)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def create(self, entity: T) -> T | None:
        self.session.add(entity)
        await self.session.flush()
        return entity

    async def delete(self, entity: T) -> None:
        await self.session.delete(entity)
        await self.session.flush()

    async def update(self, entity: T) -> T:
        self.session.add(entity)
        await self.session.flush()
        return entity