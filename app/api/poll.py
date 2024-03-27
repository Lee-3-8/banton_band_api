from pydantic import BaseModel
from json import dumps
from typing import List
from fastapi import APIRouter

router = APIRouter(
    prefix="/poll",
    tags=["poll"],
    responses={404: {"description": "Not found"}},
)

# TODO: req,res 분리


class Poll(BaseModel):
    id: int | None
    title: str
    options: List[str] = []
    multiple_choice: bool = True


@router.post("/")
def create_poll(poll: Poll):
    # create poll by poll_id, poll title,
    return poll


@router.get("/")
def create_poll():
    # get all poll u can see

    # TODO pagination , pagination을 위한 model 분리도 필요
    return {"poll_list": [Poll(id=123, title="test", options=["options1", "options2"]), Poll(id=123, title="test2", options=["options1", "options2"])]}


@router.get("/{poll_id}")
def create_poll(poll_id):
    # get poll information by poll_id
    return {"poll": Poll(id=poll_id, title="test", options=["options1", "options2"])}
