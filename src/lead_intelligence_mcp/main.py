from fastapi import FastAPI
from typing import Any, AsyncGenerator
from contextlib import asynccontextmanager
from lead_intelligence_mcp.core.config import get_settings
from .db.init_db import init_db
from .db.session import engine
import uvicorn

settings = get_settings()

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, Any]:
    print("Iniciando aplicação TROCAR MENSAGEM TROCAR MENSAGEM TROCAR MENSAGEM TROCAR MENSAGEM TROCAR MENSAGEM ")

    await init_db()
    yield

    await engine.dispose()
    print("Finalizando aplicação TROCAR MENSAGEM TROCAR MENSAGEM TROCAR MENSAGEM TROCAR MENSAGEM TROCAR MENSAGEM ")

app=FastAPI(
    title=settings.APP_NAME,
    lifespan=lifespan,
)

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok", "app": settings.APP_NAME}

def main() -> None:
    uvicorn.run(
        "lead_intelligence_mcp.main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.APP_RELOAD
    )

if __name__ == "__main__":
    main()