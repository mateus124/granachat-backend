from fastapi import FastAPI
from db.base import Base
from db.session import engine

from api.chat import router as chat_router
from api.summary import router as summary_router

Base.metadata.create_all(bind=engine)

tags_metadata = [
    {
        "name": "Chat",
        "description": "Operações de envio de mensagens",
    },
    {
        "name": "ProdSummaryuto",
        "description": "Operações de relatórios",
    },
]

app = FastAPI(
    title="Granachat API",
    openapi_tags=tags_metadata,
    description="API de controle financeiro via chat",
    version="0.1.0"
)

@app.get("/")
def healthcheck():
    return {"status": "Granachat API ok"}

app.include_router(chat_router)
app.include_router(summary_router)