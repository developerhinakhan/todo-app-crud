from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models,schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post ("/todos", response_model= schemas.TodoResponse)
def create_todo(todo: schemas.TodoCreate, db: Session= Depends(get_db)):
    new_todo = models.Todo (title= todo.title, description= todo.description)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@app.get ("/todos" ,response_model= list[schemas.TodoResponse])
def get_todos(db: Session=Depends(get_db)):
    return db.query (models.Todo).all()

@app.get("/todos/{todo_id}",response_model= schemas.TodoResponse)
def get_todo(todo_id:int,db:Session=Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404,detail="Todo not found")
    return todo

@app.put("/todos/{todo_id}",response_model= schemas.TodoResponse)
def update_todo(todo_id: int, updates: schemas.TodoUpdate, db: Session= Depends(get_db)):
    todo= db.query(models.Todo).filter(models.Todo.id==todo_id).first() 
    if not todo:
        raise HTTPException(status_code=404,detail="Todo not found")
    for key,value in updates.model_dump(exclude_unset = True).items():
        setattr(todo,key,value)
    db.commit()
    db.refresh(todo)
    return todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted successfully"}