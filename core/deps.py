from typing import Generator
from sqlalchemy.ext.asyncio import AssyncSession
from core.database import Session

async def get_session() -> Generator:
    session: AssyncSession = Session()

    try:
        yield session
    finally:
        await session.close()