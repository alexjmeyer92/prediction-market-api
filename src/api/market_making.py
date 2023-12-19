from fastapi import APIRouter

from src.db_client.market_db_client import markets_collection
from src.data_models.market_making_model import MarketPricingResponseModel, PricesModel
from src.data_models.market_model import MarketModel

from numpy import mean

router: APIRouter = APIRouter()


@router.get("/markets/prices", status_code=200, response_model=MarketPricingResponseModel)
async def check_market_prices(market_name: str):
    """
    calculates and returns the current market price for any condition in the market
    using a double auction market averaging mechanism
    """
    db_response = markets_collection.find_one({'_id': market_name})
    market = MarketModel(**db_response)

    market_conditions = []
    for condition in market.conditions:
        condition.buy.sort(key=lambda x: x.price, reverse=True)
        condition.sell.sort(key=lambda x: x.price)

        ordered_bid_pairs = zip(condition.buy, condition.sell)
        eligible_bids = [x for x in ordered_bid_pairs if x[0].price >= x[1].price]
        if eligible_bids:
            condition_price = mean([eligible_bids[-1][0].price, eligible_bids[-1][1].price])
        else:
            condition_price = 0
        market_conditions.append(
                PricesModel(
                        condition_name=condition.name,
                        condition_price=condition_price
                )
        )

    return MarketPricingResponseModel(
            market_name=market.name,
            market_id=market.market_id,
            market_question=market.question,
            conditions=market_conditions
    )
