from sqlalchemy import Table, Integer, ForeignKey, UUID
from sqlalchemy.testing.schema import Column

from app.db.session import Base

meeting_participants = Table(
    'user_role_association',
    Base.metadata,
    Column('meeting_id', Integer, ForeignKey('meetings.id')),
    Column('user_id', UUID, ForeignKey('users.id'))
)
