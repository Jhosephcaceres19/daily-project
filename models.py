from sqlalchemy import Column, Integer, String, Text, Date, DateTime, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    role = Column(String(20), default="member")  # "admin" o "member"
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    dailies_created = relationship("Daily", back_populates="creator")
    responses = relationship("DailyResponse", back_populates="user")


class Daily(Base):
    __tablename__ = "dailies"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, unique=True, nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    creator = relationship("User", back_populates="dailies_created")
    responses = relationship("DailyResponse", back_populates="daily")


class DailyResponse(Base):
    __tablename__ = "daily_responses"
    __table_args__ = (UniqueConstraint('daily_id', 'user_id', name='_user_daily_uc'),)

    id = Column(Integer, primary_key=True, index=True)
    daily_id = Column(Integer, ForeignKey("dailies.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    did_today = Column(Text, nullable=False)
    do_tomorrow = Column(Text, nullable=False)
    blockers = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    daily = relationship("Daily", back_populates="responses")
    user = relationship("User", back_populates="responses")
