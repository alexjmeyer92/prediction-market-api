from fastapi import APIRouter

from src.data_models.market_model import BidRequestModel, BidResponseModel
from src.db_client.market_db_client import markets_collection

router: APIRouter = APIRouter()


@router.post("/bid", status_code=201, response_model=BidResponseModel)
async def submit_bid(bid_data: BidRequestModel) -> BidResponseModel:
    """
    allows a market user to submit a bid for a market condition
    """

    field_str = f"conditions.$[condObj].{bid_data.bid_type}"

    # @todo use the update response and error handle the response model if update isn't successful
    update_response = markets_collection.update_one(
            filter={"name": bid_data.market_name},
            update={"$push": {field_str: bid_data.bid.dict()}},
            upsert=False,
            array_filters=[{"condObj.name": bid_data.condition}]

    )

    # @todo when a bid is submitted should it automatically try to resolve the market
    return BidResponseModel(
            message="bid submission successful",
            success=True,
            bid_data=bid_data
    )
