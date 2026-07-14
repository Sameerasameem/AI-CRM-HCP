from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from database import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    hcp_name = Column(String, nullable=False)

    details = Column(Text, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class HCP(Base):
    __tablename__ = "hcps"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    speciality = Column(String)

    hospital = Column(String)

    location = Column(String)

    phone = Column(String)