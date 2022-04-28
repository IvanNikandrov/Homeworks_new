from fastapi import FastAPI
from pydantic import constr

from items_views import router as items_router
from users.api import router as users_router
app = FastAPI()

app.include_router(users_router)
app.include_router(items_router)

@app.get('/')
def root():
    """
    Пример для докс

    :return:
    """
    return {'message': 'Hello world! and Go!'}


@app.get('/hello')
def hello_view(name: constr(min_length=3) = 'OTUS'):
    return {'message': f'Hello{name}'}


@app.get('/add')
def add(a: int, b: int):
    return {'a': a, 'b': b, 'sum': a + b}


@app.get('/mypage')
def mypage():
    return {'message':'Hello this is my page, for training fastapi learning'}

@app.get('/ping')
def ping():
    return {"message": "pong"}
