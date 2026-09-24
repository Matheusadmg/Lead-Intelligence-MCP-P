import json
from pathlib import Path
from sqlalchemy import select, func

from .models.base import Base
from .models.historico_interacoes_model import HistoricoInteracoesModel
from .models.leads_model import LeadsModel
from .session import async_session, engine

SEED_PATH = Path(__file__).resolve().parents[3] / "seeds" / "mock_leads.json"

async def init_seed_leads() -> None:
    if not Path(SEED_PATH).exists():
        return #TODO error

    with open(SEED_PATH, encoding="utf-8") as seed:
        json_seed = json.load(seed)

        async with async_session() as session:
            total_leads = await session.scalar(select(func.count()).select_from(LeadsModel))
            if total_leads:
                print("Banco já está populado")
                return

            print("Adicionando seeds mocadas ao banco...")

            new_leads = [
                LeadsModel(
                    id_pessoa=item["id_pessoa"],
                    nome=item["nome"],
                    email=item["email"],
                    cargo=item["cargo"],
                    empresa=item["empresa"],
                    setor=item["setor"],
                    score_atual=item["score_atual"],
                    cenario_teste=item["cenario_teste"],
                    historico=[
                        HistoricoInteracoesModel(
                            acao=h["acao"],
                            item=h["item"],
                            data=h["data"]
                        )
                        for h in (item.get("historico_interacoes") or [])
                    ]
                )
                for item in json_seed
            ]

            session.add_all(new_leads)
            await session.commit()
            print("Novos leads carregados com sucesso!")

async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await init_seed_leads()