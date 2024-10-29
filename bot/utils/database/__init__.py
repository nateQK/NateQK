from alembic.config import Config
from alembic import command
from .. import configDB as config



# NOTE: Setup alembic config
alembic_cfg = Config()
alembic_cfg.set_main_option("script_location", "bot/utils/database/alembic")
alembic_cfg.set_main_option("prepend_sys_path", ".")
if not config.getPassword == "":
    alembic_cfg.set_main_option("sqlalchemy.url", f'{config.getEngine}://{config.getUsername}:{config.getPassword}@{config.getHost}:{config.getPort}/{config.getDatabase}')
else:
    alembic_cfg.set_main_option("sqlalchemy.url", f'{config.getEngine}://{config.getUsername}@{config.getHost}:{config.getPort}/{config.getDatabase}')



# NOTE: Upgrade database tables to latest version
command.upgrade(alembic_cfg, "head")

# WARN: This file still needs to initialized the database, this will be done by calling connect from the database file


