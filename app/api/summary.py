from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date

from db.deps import get_db
from models.transaction import Transaction

router = APIRouter(prefix="/summary", tags=["Summary"])

@router.get("/month")
def month_summary(
    year: int = Query(..., description="Ano (ex: 2026)"),
    month: int = Query(..., ge=1, le=12, description="Mês (1-12)"),
    db: Session = Depends(get_db)
):
    start_date = date(year, month, 1)

    if month == 12:
        end_date = date(year + 1, 1, 1)
    else:
        end_date = date(year, month + 1, 1)

    results = (
        db.query(
            Transaction.categoria,
            func.sum(Transaction.valor)
        )
        .filter(
            Transaction.tipo == "despesa",
            Transaction.data >= start_date,
            Transaction.data < end_date
        )
        .group_by(Transaction.categoria)
        .all()
    )

    return {categoria: total for categoria, total in results}
