from typing import List

from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

database = []


class Events(BaseModel):
    nome: str
    dono: str
    descrica: str
    data: str
    quantidade_ingressos: int
    foi_vendido: bool
    data_validade: str


@app.get('/')
async def hello_word() -> str:
    return 'Hello World 🌎🌍🌏'


@app.post('/event', response_model=Events)
async def criar_evento(event: Events):
    database.append(event)

    return event


@app.get('/event')
async def ler_todos_os_eventos() -> List[Events]:
    return database
