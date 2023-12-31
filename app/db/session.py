from contextvars import ContextVar, Token
from typing import Union

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from app.config import config

session_context: ContextVar[str] = ContextVar("session_context")


def get_session_context() -> str:
    return session_context.get()


def set_session_context(session_id: str) -> Token:
    return session_context.set(session_id)


def reset_session_context(context: Token) -> None:
    session_context.reset(context)


engines = {"main": create_engine(config.main_database.connection_string(), pool_recycle=3600)}


class RoutingSession(Session):
    def get_bind(self, **kwargs):  # pylint: disable=unused-argument
        return engines['main']


async_session_factory = sessionmaker(
    class_=AsyncSession,
    sync_session_class=RoutingSession,
)
session: Union[AsyncSession, async_scoped_session] = async_scoped_session(
    session_factory=async_session_factory,  # noqa
    scopefunc=get_session_context,
)
Base = declarative_base()
