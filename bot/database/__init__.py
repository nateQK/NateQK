from alembic.config import Config
from alembic import command
from bot.config import Config as fullConf
#from loguru import logger

config = fullConf.config


# NOTE: Setup alembic config
alembic_cfg = Config()
alembic_cfg.set_main_option("script_location", "bot/database/alembic")
alembic_cfg.set_main_option("prepend_sys_path", ".")


if not str(config.database.password) == str(""):
    alembic_cfg.set_main_option("sqlalchemy.url", f'{config.database.engine}+asyncpg://{config.database.username}:{config.database.password}@{config.database.host}:{config.database.port}/{config.database.database}')
else:
    alembic_cfg.set_main_option("sqlalchemy.url", f'{config.database.engine}+asyncpg://{config.database.username}@{config.database.host}:{config.database.port}/{config.database.database}')



# NOTE: Upgrade database tables to latest version
command.upgrade(alembic_cfg, "head")



