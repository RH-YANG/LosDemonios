from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
import bcrypt
import datetime
import os
import jwt
from dotenv import load_dotenv

import model.dao.golem_dao as golem_dao
import model.db as db
from model.schemas.domain_schema import Golem



load_dotenv()

key = os.getenv("JWT_SECRET_KEY")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="golem/login")



@db.connection_manager
def login(conn, cur, rq_golem: Golem):
    # 1. 계정 조회
    db_golem = golem_dao.select_by_email(cur, rq_golem)
    if not db_golem:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "User Not Found")

    # 2. 비밀번호 검증
    request_pwd = rq_golem.pwd.encode("utf-8")
    fetched_pwd = db_golem.pwd.encode("utf-8")
    match = bcrypt.checkpw(request_pwd, fetched_pwd)
    if not match:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Password Not Matched")
    
    return db_golem



def generate(gol_seq):
    # 1. 토큰 생성
    access_payload = {
        "gol_seq": gol_seq,
        "refresh" : False,
        "exp" : datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)
    }
    access_token = jwt.encode(access_payload, key, "HS256")

    refresh_payload = {
        "gol_seq": gol_seq,
        "refresh" : True,
        "exp" : datetime.datetime.now() + datetime.timedelta(days=3)
    }
    refresh_token = jwt.encode(refresh_payload, key, "HS256")

    # 2. 리프레쉬 토큰 DB 저장
    golem = Golem(gol_seq=gol_seq, token=refresh_token)
    update_refresh(golem)
    
    return access_token, refresh_token



@db.connection_manager
def update_refresh(conn, cur, golem: Golem):
    result = golem_dao.update_refresh(cur, golem)

    if not result:
        db.fail_routine(conn)
    conn.commit()



# TODO : async 필요성 재확인
# 토큰이 헤더에 존재하는지, bearer로 시작하는지 검증
def authenticate(
    token: str = Depends(oauth2_scheme) 
):
    payload = verify_token(token)
    
    return payload


# 토큰의 유효성 검증
def verify_token(token: str):
    try:
        payload = jwt.decode(token, key, algorithms=["HS256"]) 

        return payload
    
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token",
            headers={"WWW-Authenticate": "Bearer"},
        )