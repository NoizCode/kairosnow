from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from . import db
from sqlalchemy import MetaData

scheduler = BackgroundScheduler()

def refresh_db(session):
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print("clearing tables")
        session.execute(table.delete())
    session.commit()