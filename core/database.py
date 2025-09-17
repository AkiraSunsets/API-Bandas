from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from core.configs import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL)

Session = AsyncEngine = sessionmaker(
    autocommit = False, #não fica autocomitando
    autoflush = False,
    expire_on_commit = False, #só expira a sessão quando fechar o arquivo
    class_ = AsyncSession,
    bind= engine
)