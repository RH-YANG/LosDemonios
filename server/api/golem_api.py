from fastapi import APIRouter, Depends
from dotenv import load_dotenv

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

import service.golem_service as golem_service
from model.schemas.domain_schema import Golem



router = APIRouter(prefix="/golem", 
                   tags=["golem"])

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="golem/login")

# dotenv_path = "../.env"
# load_dotenv(dotenv_path)


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
    gol_seq = golem_service.insert(golem)

    return gol_seq



# @router.post("/login")
# def login(
#     request: OAuth2PasswordRequestForm = Depends()
# ):
#     golem = Golem(email=request.username, pwd=request.password)
#     db_golem = token_service.login(golem) # email, pw 검증
#     access_token, refresh_token = token_service.generate(db_golem) # 토큰 생성
    
#     return  {
#         "email":golem.email,
#         "access_token":access_token,
#         "refresh_token":refresh_token
#     } 