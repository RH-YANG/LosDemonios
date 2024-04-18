from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Golem(BaseModel):
    gol_seq: int = 0
    email: str = ""
    pwd: str = ""
    nickname: str = ""
    profile_img: str = ""
    gender: str = ""
    token: str = ""
    join_at: Optional[datetime] = None
    last_at: Optional[datetime] = None