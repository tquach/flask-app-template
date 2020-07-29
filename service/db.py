from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from service import app

engine = create_engine(app.config['DATABASE_URI'], convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


@app.cli.command('init-db')
def init_db():
    # import all modules
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


@app.after_request
def after_request(response):
    db_session.remove()
    return response
