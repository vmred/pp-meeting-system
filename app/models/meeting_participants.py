from sqlalchemy import UUID, ForeignKey, Integer, Table
from sqlalchemy.testing.schema import Column

from app.db.session import Base

meeting_participants = Table(
    'meeting_participants',
    Base.metadata,
    Column('meeting_id', Integer, ForeignKey('meetings.id')),
    Column('user_id', UUID, ForeignKey('users.id')),
)
