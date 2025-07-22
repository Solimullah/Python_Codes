from sqlalchemy.orm import Session
from .. import db, schemas

def get_budgets_by_owner(db: Session, owner_id: int, skip: int = 0, limit: int = 100):
    return db.query(db.models.BudgetCategory).filter(db.models.BudgetCategory.owner_id == owner_id).offset(skip).limit(limit).all()

def create_budget(db: Session, budget: schemas.budget.BudgetCreate, owner_id: int):
    db_budget = db.models.BudgetCategory(**budget.dict(), owner_id=owner_id)
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    return db_budget

def update_budget(db: Session, budget_id: int, budget: schemas.budget.BudgetCreate, owner_id: int):
    db_budget = db.query(db.models.BudgetCategory).filter(db.models.BudgetCategory.id == budget_id, db.models.BudgetCategory.owner_id == owner_id).first()
    if db_budget:
        for key, value in budget.dict().items():
            setattr(db_budget, key, value)
        db.commit()
        db.refresh(db_budget)
    return db_budget

def delete_budget(db: Session, budget_id: int, owner_id: int):
    db_budget = db.query(db.models.BudgetCategory).filter(db.models.BudgetCategory.id == budget_id, db.models.BudgetCategory.owner_id == owner_id).first()
    if db_budget:
        db.delete(db_budget)
        db.commit()
    return db_budget
