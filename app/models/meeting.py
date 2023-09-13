from typing import List

from sqlalchemy import UUID, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class Meeting(Base):
    __tablename__ = 'meetings'

    # columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    location = Column(String(100))
    time = Column(DateTime)

    # relationships
    comment_relationship: Mapped[List["Comment"]] = relationship()
    creator_user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    users = relationship('User', secondary='meeting_participants', back_populates='meetings')
