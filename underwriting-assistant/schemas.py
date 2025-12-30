from pydantic import BaseModel
from typing import List


class UnderwritingResult(BaseModel):
    risk_level: str
    risk_score: int
    key_risk_factors: List[str]
    underwriting_summary: str
    recommendation: str
