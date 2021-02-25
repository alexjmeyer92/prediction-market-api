from fastapi import APIRouter
from pydantic import BaseModel

from src.db_client.market_db_client import database

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
    """
    Gives a health check that confirms the service is running & healthy
    """

    db_collections = database.list_collection_names()
    if 'markets' in db_collections:

        return CoreResponse(
                message="Prediction Market API is running and healthy"
        )
    else:
        return CoreResponse(
                message="Prediction Market API is running but cannot access the DB."
        )
