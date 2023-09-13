from sqlalchemy import UUID, BigInteger, Column, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class Expense(Base):
    __tablename__ = 'expenses'

    # columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(BigInteger, nullable=False, default=0)

    # relationships
    owner_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    meeting_id: Mapped[Integer] = mapped_column(ForeignKey('meetings.id'))
    expense_participants = relationship('User', secondary='expense_participants', back_populates='expenses')
