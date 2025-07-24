from pydantic import BaseModel

class TransactionBase(BaseModel):
    description: str
    amount: float

class TransactionCreate(TransactionBase):
    category_id: int

class Transaction(TransactionBase):
    id: int
    owner_id: int
    category_id: int

    class Config:
        #orm_mode = True
        from_attributes = True
