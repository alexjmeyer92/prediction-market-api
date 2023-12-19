from typing import List

from fastapi import APIRouter
from src.data_models.market_model import MarketModel, MarketsResponse

from src.db_client import market_db_client

router: APIRouter = APIRouter()


# @todo error handling in market management endpoints

@router.post("/markets", status_code=201, response_model=MarketsResponse)
async def create_markets(markets_data: MarketModel) -> MarketsResponse:
    """
    A post request to /markets will create a new market for each market submitted
    """
    market_id = market_db_client.database.markets.insert_one(markets_data.dict(by_alias=True))

    return MarketsResponse(message="market {} created successfully".format(market_id))


@router.delete("/markets", status_code=200, response_model=MarketsResponse)
async def delete_markets(market_name: str) -> MarketsResponse:
    """
    a delete request to /markets will remove the market by name
    """
    db_response = market_db_client.markets_collection.remove({"name": market_name})

    return MarketsResponse(message="Market {} deleted".format(db_response))


@router.get("/markets", status_code=200, response_model=List[MarketModel])
async def get_all_markets() -> List[MarketModel]:
    """
    a get request to the markets endpoint will return a paginated list
    of all currently active markets
    """
    db_response = market_db_client.database.markets.find()
    markets = []
    for market in db_response:
        markets.append(MarketModel(**market))

    return markets
