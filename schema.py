from pydantic import BaseModel
from datetime import datetime
class pdf(BaseModel):
    #2
    id:int
    filename:str
    content:str
    status:str
    created_at:datetime
