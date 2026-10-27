from fastapi import APIRouter

router = APIRouter()

@router.get("/itemss")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}