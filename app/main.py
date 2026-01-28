from fastapi import FastAPI

from api.chat import router as chat_router

app = FastAPI(
    title="Granachat API",
    description="API de controle financeiro via chat",
    version="0.1.0"
)

@app.get("/")
def healthcheck():
    return {"status": "Granachat API ok"}

app.include_router(chat_router)