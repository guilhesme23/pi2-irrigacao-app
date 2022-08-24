from fastapi import Body, APIRouter

router = APIRouter()

irrigate = False

@router.get("/bot", tags = ["Bot"])
def get_start():
    message = "Stop irrigation"
    if irrigate:
        message = "Start irrigation"
    return {"message": message, "data": irrigate}

@router.post("/bot", tags = ["Bot"])
def post_start(start: bool):
    irrigate = start
    message = "Stop irrigation"
    if irrigate:
        message = "Start irrigation"
    return {"message": message, "data": irrigate}
