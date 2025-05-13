from fastapi import FastAPI

from TodoApp.database import engine
from TodoApp.todo_models import models

app = FastAPI()

# from TodoApp.todo_models import models
models.Base.metadata.create_all(bind=engine)
