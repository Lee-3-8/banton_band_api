
from scrapper import groove
from fastapi import APIRouter

router = APIRouter(
    prefix="/groove",
    tags=["groove"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_reservation_info():
    groove.get_status()
    return {"message": "get groove png"}
