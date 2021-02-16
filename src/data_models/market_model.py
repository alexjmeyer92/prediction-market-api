from pydantic import BaseModel
from uuid import UUID

from typing import List


class BidModel(BaseModel):
    user: str
    bid_id: UUID
    price: float


class ConditionsModel(BaseModel):
    name: str
    buy_bids: List[BidModel] = []
    sell_bids: List[BidModel] = []

# @todo figure out how to automatically set the _id attribute in mongo to be the market name
class MarketModel(BaseModel):
    name: str
    question: str
    active: bool = True
    conditions: List[ConditionsModel] = []


class MarketsResponse(BaseModel):
    message: str
