from fastapi import APIRouter

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/")
def chat(message: str):
    return {
        "resposta": f"Mensagem recebida: {message}"
    }
