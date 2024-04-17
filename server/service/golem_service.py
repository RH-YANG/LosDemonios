import bcrypt

import model.dao.golem_dao as golem_dao
import model.db as db
from model.schemas.domain_schema import Golem



@db.connection_manager
def check_duplicate(conn, cur, item, value):
    is_available = golem_dao.check_duplicate(cur, item, value)

    return is_available


def encrypt_pwd(pwd):
    encoded_pwd = pwd.encode("utf-8")
    salt = bcrypt.gensalt()
    encrypt_pwd = bcrypt.hashpw(encoded_pwd, salt).decode("utf-8")   

    return encrypt_pwd


@db.connection_manager
def insert(conn, cur, golem: Golem):
    golem.pwd = encrypt_pwd(golem.pwd) # 비밀번호 암호화

    result = golem_dao.insert(cur, golem) # DB 삽입
    gol_seq = golem_dao.current_seq(cur) # 식별자 조회

    if not (result or gol_seq):
        db.fail_routine(conn)

    conn.commit()
    return gol_seq



# @db.connection_manager
# def update_pwd(conn, cur, golem: Golem):
#     golem.pwd = encrypt_pwd(golem.pwd)

#     result = golem_dao.update_pwd(cur, golem)
#     if not result:
#         db.fail_routine(conn)
    
#     conn.commit()    