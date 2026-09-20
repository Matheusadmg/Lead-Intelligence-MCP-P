from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker, AsyncSession
from ..core.config import get_settings

settings = get_settings()

engine: AsyncEngine = create_async_engine(
    url= settings.DATABASE_URL,
    echo=settings.POSTGRES_ECHO,
    pool_pre_ping=True
)

async_session: async_sessionmaker[AsyncSession] = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise