from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    hcp_name = Column(String)
    interaction_type = Column(String)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)


class HCP(Base):
    __tablename__ = "hcps"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    specialty = Column(String)
    hospital = Column(String)
    phone = Column(String)
    email = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)