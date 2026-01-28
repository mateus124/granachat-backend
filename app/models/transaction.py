from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from db.base import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    tipo = Column(String) # gasto, ganho, poupanca
    valor = Column(Float)
    categoria = Column(String)
    descricao = Column(String)
    data = Column(Date)