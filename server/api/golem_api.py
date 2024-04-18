from fastapi import APIRouter, Depends

from fastapi.security import OAuth2PasswordRequestForm

import service.golem_service as golem_service
import service.token_service as token_service
from model.schemas.domain_schema import Golem



router = APIRouter(prefix="/golem", 
                   tags=["golem"])



@router.get("/available")
def check_duplicate(
    email: str = "",
    nickname: str = ""
):
    if email:
        is_available = golem_service.check_duplicate("email", email)
    elif nickname:
        is_available = golem_service.check_duplicate("nickname", nickname)
    
    return is_available



@router.post("/join")
def occupy(
    golem: Golem
):
    gol_seq = golem_service.insert(golem) # db 삽입
    access_token, refresh_token = token_service.generate(gol_seq) # 토큰 생성
    
    response = {
        "access_token": access_token,
        "refresh_token": refresh_token
    }

    return response



@router.post("/login")
def login(
    request: OAuth2PasswordRequestForm = Depends()
):
    rq_golem = Golem(email=request.username, pwd=request.password)
    db_golem = token_service.login(rq_golem) # email, pwd 검증
    access_token, refresh_token = token_service.generate(db_golem.gol_seq) # 토큰 생성
    
    response = {
        "nickname": db_golem.nickname,
        "access_token": access_token,
        "refresh_token": refresh_token
    }

    return response



# 작성중
@router.put("/update")
def update(
    golem: Golem,
    payload = Depends(token_service.authenticate)
):
    golem.gol_seq = payload['gol_seq']
    
    golem_service.update(golem)