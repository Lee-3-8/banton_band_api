from pydantic import BaseModel
from typing import List

class Poll(BaseModel):
    id: int | None
    title: str
    options: List[str] = []
    multiple_choice: bool = True
