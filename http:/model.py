from typing import Optional

from pydantic import BaseModel


class ClassifyRequest(BaseModel):
    card_1: Optional[float]
    card_2: Optional[float]
    car_d5: Optional[float]
    addr_1: Optional[float]
    transaction_amt: Optional[float]
    p_email_domain: Optional[str]
    c1: Optional[float]
    d2: Optional[float]
    d15: Optional[float]
    v313: Optional[float]
    day: Optional[float]
    hour: Optional[float]
    month: Optional[float]
    dow: Optional[float]