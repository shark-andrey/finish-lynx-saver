import sqlalchemy as sa

from sqlalchemy.orm import sessionmaker

from . import config

engine = sa.create_engine(config.db_url)

DbSession = sessionmaker(engine)
