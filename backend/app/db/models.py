from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    budgets = relationship("BudgetCategory", back_populates="owner")
    transactions = relationship("Transaction", back_populates="owner")

class BudgetCategory(Base):
    __tablename__ = "budget_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    allocated_amount = Column(Float)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="budgets")
    transactions = relationship("Transaction", back_populates="category")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    amount = Column(Float)
    category_id = Column(Integer, ForeignKey("budget_categories.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))

    category = relationship("BudgetCategory", back_populates="transactions")
    owner = relationship("User", back_populates="transactions")
