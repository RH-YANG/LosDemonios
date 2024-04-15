import os
import psycopg2
import logging
from psycopg2.extras import LoggingConnection
from dotenv import load_dotenv
from fastapi import status, HTTPException



dotenv_path = "../.env"
load_dotenv(dotenv_path)

host = os.getenv("SERVER_ADDR")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PWD")



def connection_manager(func):
    def wrapper(*args, **kwargs):

        conn = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password,
        )
        cur = conn.cursor()

        try :
            return func(conn, cur, *args, **kwargs)

        finally:
            cur.close()
            conn.close()

    return wrapper



# 최종 쿼리 로그출력 (개발용)
def connection_with_log(func):
    def wrapper(*args, **kwargs):
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger(__name__)

        conn = psycopg2.connect(
            connection_factory=LoggingConnection,
            host=host,
            port=port,
            database=database,
            user=user,
            password=password,
        )

        conn.initialize(logger)

        cur = conn.cursor()

        try :
            return func(conn, cur, *args, **kwargs)

        finally:
            cur.close()
            conn.close()

    return wrapper



def fail_routine(conn):
    conn.rollback() 
    raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE, "DML Failure without errors")