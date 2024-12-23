from alembic.config import Config
from alembic import command
from .. import configDB as config
#from loguru import logger



# NOTE: Setup alembic config
alembic_cfg = Config()
alembic_cfg.set_main_option("script_location", "bot/utils/database/alembic")
alembic_cfg.set_main_option("prepend_sys_path", ".")


if not str(config.getPassword) == str(""):
    alembic_cfg.set_main_option("sqlalchemy.url", f'{config.getEngine()}+asyncpg://{config.getUsername()}:{config.getPassword()}@{config.getHost()}:{config.getPort()}/{config.getDatabase()}')
else:
    alembic_cfg.set_main_option("sqlalchemy.url", f'{config.getEngine()}+asyncpg://{config.getUsername()}@{config.getHost()}:{config.getPort()}/{config.getDatabase()}')



# NOTE: Upgrade database tables to latest version
command.upgrade(alembic_cfg, "head")



