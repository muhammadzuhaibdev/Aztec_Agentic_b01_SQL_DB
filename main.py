from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from config.db_connection import SessionLocal
from models.todo_model import Todo

app = FastAPI()

class CreateTodo(BaseModel):
    title: str
    description: str
    status: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/createTodo')
def createTodo(todoData: CreateTodo, db: Session =  Depends(get_db)):
    try:
        print(todoData)
        
        new_todo = Todo(title=todoData.title, description=todoData.description, status=todoData.status)
        
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)
        
        return {
            "status": "success",
            "data": new_todo,
            "message": "Todo Created Successfully!"
        }
    except Exception as e:
        return {
            "status": "error",
            "data": [],
            "message": str(e)
        }

@app.get('/getTodos')
def getTodos(db: Session = Depends(get_db)):
    try:
        
        todosData = db.query(Todo).all()
        
        return {
            "status": "success",
            "data": todosData,
            "message": "Todos data fetched successfully!"
        }
    except Exception as e:
        return {
            "status": "error",
            "data": [],
            "message": str(e)
        }
        
@app.get('/getSingleTodo/{status}')
def getTodos(status: str, db: Session = Depends(get_db)):
    try:
        
        todosData = db.query(Todo).where(Todo.status == status).all()
        # todosData = db.query(Todo).where(Todo.status == status).count()
        # todosData = db.query(Todo).where(Todo.status == status).first()
        
        return {
            "status": "success",
            "data": todosData,
            "message": "Todo fetched successfully!"
        }
    except Exception as e:
        return {
            "status": "error",
            "data": [],
            "message": str(e)
        }
        
        
@app.put('/updateTodo/{id}')
def getTodos(id: int, updatedData: CreateTodo,  db: Session = Depends(get_db)):
    try:
        
        findTodo = db.query(Todo).filter(Todo.id == id).first()
        
        if not findTodo:
            return {"msg": "Todo Not Found"}
        

        findTodo.title = updatedData.title
        findTodo.description = updatedData.description
        findTodo.status = updatedData.status
        
        
        db.commit()
        db.refresh(findTodo)
        
        return {
            "status": "success",
            "message": "Todo Updated successfully!"
        }
    except Exception as e:
        return {
            "status": "error",
            "data": [],
            "message": str(e)
        }
        

@app.delete('/deleteTodo/{id}')
def getTodos(id: int, db: Session = Depends(get_db)):
    try:
        
        findTodo = db.query(Todo).filter(Todo.id == id).first()
        
        if not findTodo:
            return {"msg": "Todo Not Found"}
        
        db.delete(findTodo)
        db.commit()
        
        return {
            "status": "success",
            "message": "Todo Deleted successfully!"
        }
    except Exception as e:
        return {
            "status": "error",
            "data": [],
            "message": str(e)
        }
        

@app.get("/")
def server_testing():
    return {"msg": "server is up & running."}