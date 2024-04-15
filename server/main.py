from fastapi import FastAPI, APIRouter

from api.golem_api import router as golem_router


app = FastAPI()


router = APIRouter()
router.include_router(golem_router)
app.include_router(router)