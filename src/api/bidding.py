from fastapi import APIRouter, status, Response

from src.data_models.market_model import BidRequestModel, BidResponseModel
from src.db_client.market_db_client import markets_collection

router: APIRouter = APIRouter()


@router.post("/bid", status_code=201, response_model=BidResponseModel, responses={400: {"model": BidResponseModel}})
async def submit_bid(bid_data: BidRequestModel, response: Response) -> BidResponseModel:
    """
    allows a market user to submit a bid for a market condition
    """

    field_str = f"conditions.$[condObj].{bid_data.bid_type}"

    update_response = markets_collection.update_one(
            filter={"name": bid_data.market_name},
            update={"$push": {field_str: bid_data.bid.dict()}},
            upsert=False,
            array_filters=[{"condObj.name": bid_data.condition}]

    )

    if update_response.matched_count == update_response.modified_count and update_response.acknowledged is True:

        return BidResponseModel(
                message="bid submission successful",
                successful=True,
                bid_data=bid_data
        )
    elif update_response.matched_count == 0:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return BidResponseModel(
                message="Bid submission failed, requested market does not exist",
                successful=False,
                bid_data=bid_data
        )
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return BidResponseModel(
                message="Bid submission failed",
                successful=False,
                bid_data=bid_data
        )
