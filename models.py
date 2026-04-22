from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base   # assuming you defined Base elsewhere

class PDF(Base):
    __tablename__ = "pdf"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    content = Column(String, nullable=True)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)