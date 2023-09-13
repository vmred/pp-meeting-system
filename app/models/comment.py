from sqlalchemy import UUID, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base
from app.db.mixins.timestamp import TimestampMixin


class Comment(Base, TimestampMixin):
    __tablename__ = 'comments'

    # columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    comment = Column(String(255), nullable=True)

    # relationships
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    meeting_id: Mapped[Integer] = mapped_column(ForeignKey('meetings.id'))
