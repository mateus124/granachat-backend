from sqlalchemy import Column, Integer, String, Float, Date
from app.db.base import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String) # gasto, ganho, poupanca
    valor = Column(Float)
    categoria = Column(String)
    descricao = Column(String)
    data = Column(Date)