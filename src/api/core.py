from fastapi import APIRouter
from pydantic import BaseModel

router: APIRouter = APIRouter()


# define root response message
class CoreResponse(BaseModel):
    message: str


@router.get("/", response_model=CoreResponse)
async def root() -> CoreResponse:
    return CoreResponse(
            message="This is the prediction market api"
    )


@router.get("/health", response_model=CoreResponse)
async def health_check() -> CoreResponse:
    return CoreResponse(
            message="Prediction Market API is running and healthy"
    )
