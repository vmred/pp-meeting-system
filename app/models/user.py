from typing import List
from uuid import uuid4

from sqlalchemy import Column, UUID, String
from sqlalchemy.orm import Mapped, relationship

from app.db.session import Base


class User(Base):
    __tablename__ = 'users'

    # columns
    id = Column(UUID, primary_key=True, default=uuid4())
    email = Column(String(254), unique=True)
    password = Column(String(32))

    # relationships
    meeting_relationship: Mapped[List["Meeting"]] = relationship()
    comment_relationship: Mapped[List["Comment"]] = relationship()
