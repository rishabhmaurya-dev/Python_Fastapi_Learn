from fastapi import FastAPI
from routing import path_parameters,query_parameters,optional_parameters

app = FastAPI()

app.include_router(path_parameters.router)
app.include_router(query_parameters.router)
app.include_router(optional_parameters.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}   