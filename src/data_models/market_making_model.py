from pydantic import BaseModel
from uuid import UUID
from typing import List


class PricesModel(BaseModel):
    condition_name: str
    condition_price: float


class MarketPricingResponseModel(BaseModel):
    market_name: str
    market_id: UUID
    market_question: str
    conditions: List[PricesModel]
