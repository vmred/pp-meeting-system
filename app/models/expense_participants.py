from sqlalchemy import UUID, ForeignKey, Integer, Table
from sqlalchemy.testing.schema import Column

from app.db.session import Base

expense_participants = Table(
    'expense_participants',
    Base.metadata,
    Column('expense_id', Integer, ForeignKey('expenses.id')),
    Column('user_id', UUID, ForeignKey('users.id')),
)
