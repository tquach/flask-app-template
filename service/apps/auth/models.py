from sqlalchemy import Column, Integer, String, DateTime, func

from service import db


class Account(db.Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    username = Column(String(128), nullable=False)
    password = Column(String(32), unique=True)

    create_date = Column(DateTime, default=func.now(), nullable=False)
    last_updated = Column(DateTime, default=func.now(), nullable=False)

    def __str__(self):
        return format(
            "Account[id=%s,username=%s,password=******]" % (
                self.id, self.username))
