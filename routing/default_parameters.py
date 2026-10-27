from fastapi import APIRouter

router = APIRouter()

@router.get("/name")
async def show_name (name : str = "rishabh" ):
  return {
    "name" : name
  }