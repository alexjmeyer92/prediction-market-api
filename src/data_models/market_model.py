from pydantic import BaseModel, Field, validator
from uuid import UUID, uuid4

from typing import List, Any


class BidModel(BaseModel):
    user: str
    bid_id: UUID = uuid4()
    price: float


class BidRequestModel(BaseModel):
    market_name: str
    user: str
    condition: str
    bid_type: str
    bid: BidModel

    @validator('bid_type')
    def queue_type_validator(cls, type: str) -> str:
        assert type in ['buy', 'sell']
        return type


class BidResponseModel(BaseModel):
    message: str
    successful: bool
    bid_data: BidRequestModel


class ConditionsModel(BaseModel):
    name: str
    buy: List[BidModel] = []
    sell: List[BidModel] = []


class MarketModel(BaseModel):
    id: str = Field(alias="_id", default_factory=str)
    market_id: UUID = uuid4()
    name: str
    question: str
    active: bool = True
    closed: bool = False
    conditions: List[ConditionsModel] = []

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        self.id = self.name


class MarketsResponse(BaseModel):
    message: str
