from pydantic import BaseModel

class BudgetBase(BaseModel):
    name: str
    allocated_amount: float

class BudgetCreate(BudgetBase):
    pass

class Budget(BudgetBase):
    id: int
    owner_id: int

    class Config:
        #orm_mode = True
        from_attributes = True
