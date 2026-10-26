from fastapi import FastAPI
from routing.path_parameters import router
app = FastAPI()
app.include_router(router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}   