from pydantic import BaseModel, Field
from typing import Literal 


class DSAResponse(BaseModel):
    title:str = Field(..., min_length=3)
    topic:str = Field(..., min_length=3)
    difficulty:Literal["Easy", "Medium", "Hard"]
    approach:str = Field(..., min_length=20)
    code:str = Field(..., min_length=20)
    time_complexity:str = Field(..., min_length=3)
    space_complexity:str = Field(..., min_length=3)
