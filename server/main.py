from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from api.golem_api import router as golem_router


app = FastAPI()


router = APIRouter()
router.include_router(golem_router)
app.include_router(router)


# CORS 활성화
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 모든 원본으로부터의 요청 허용
    allow_credentials=True, # 인증정보 포함할 수 있도록 함
    allow_methods=["*"], # 모든 HTTP 메소드 허용
    allow_headers=["*"], # 모든 종류의 헤더 허용
)