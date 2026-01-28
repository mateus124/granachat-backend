from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.chat import ChatMessage
from core.parser import parse_message
from db.deps import get_db
from models.transaction import Transaction

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/")
def chat(payload: ChatMessage, db: Session = Depends(get_db)):
    try:
        data = parse_message(payload.message)

        transaction = Transaction(**data)
        db.add(transaction)
        db.commit()

        return {
            "resposta": f"Anotado: {data['tipo']} de R${data['valor']} em {data['categoria']}"
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
