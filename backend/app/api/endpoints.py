from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta

from .. import crud, schemas, auth
from ..crud import crud_task
from ..schemas import task
from ..db import database

router = APIRouter()

@router.post("/auth/register", response_model=schemas.user.User)
def register_user(user: schemas.user.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.crud_user.create_user(db=db, user=user)

from fastapi.security import OAuth2PasswordRequestForm

@router.post("/auth/login", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = crud.crud_user.get_user_by_email(db, email=form_data.username)
    if not user or not auth.jwt.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.jwt.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.jwt.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/budgets/", response_model=list[schemas.budget.Budget])
def read_budgets(skip: int = 0, limit: int = 100, current_user: schemas.user.User = Depends(auth.jwt.get_current_user), db: Session = Depends(database.get_db)):
    budgets = crud.crud_budget.get_budgets_by_owner(db, owner_id=current_user.id, skip=skip, limit=limit)
    return budgets

@router.post("/budgets/", response_model=schemas.budget.Budget)
def create_budget(budget: schemas.budget.BudgetCreate, current_user: schemas.user.User = Depends(auth.jwt.get_current_user), db: Session = Depends(database.get_db)):
    return crud.crud_budget.create_budget(db=db, budget=budget, owner_id=current_user.id)

@router.put("/budgets/{budget_id}", response_model=schemas.budget.Budget)
def update_budget(budget_id: int, budget: schemas.budget.BudgetCreate, current_user: schemas.user.User = Depends(auth.jwt.get_current_user), db: Session = Depends(database.get_db)):
    db_budget = crud.crud_budget.update_budget(db=db, budget_id=budget_id, budget=budget, owner_id=current_user.id)
    if db_budget is None:
        raise HTTPException(status_code=404, detail="Budget not found")
    return db_budget

@router.post("/tasks/", response_model=schemas.task.Task)
def create_task(task: schemas.task.TaskCreate, db: Session = Depends(database.get_db)):
    return crud.crud_task.create_task(db=db, task=task)

@router.get("/tasks/", response_model=list[schemas.task.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    tasks = crud.crud_task.get_tasks(db, skip=skip, limit=limit)
    return tasks

@router.get("/tasks/{task_id}", response_model=schemas.task.Task)
def read_task(task_id: int, db: Session = Depends(database.get_db)):
    db_task = crud.crud_task.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.put("/tasks/{task_id}", response_model=schemas.task.Task)
def update_task(task_id: int, task: schemas.task.TaskCreate, db: Session = Depends(database.get_db)):
    db_task = crud.crud_task.update_task(db=db, task_id=task_id, task=task)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.delete("/tasks/{task_id}", response_model=schemas.task.Task)
def delete_task(task_id: int, db: Session = Depends(database.get_db)):
    db_task = crud.crud_task.delete_task(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.delete("/budgets/{budget_id}", response_model=schemas.budget.Budget)
def delete_budget(budget_id: int, current_user: schemas.user.User = Depends(auth.jwt.get_current_user), db: Session = Depends(database.get_db)):
    db_budget = crud.crud_budget.delete_budget(db=db, budget_id=budget_id, owner_id=current_user.id)
    if db_budget is None:
        raise HTTPException(status_code=404, detail="Budget not found")
    return db_budget
