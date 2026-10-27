from fastapi import APIRouter

router = APIRouter()

@router.get("/items")
async def read_item(item_id: int, q: str):
    return {"item_id": item_id, "q": q} 