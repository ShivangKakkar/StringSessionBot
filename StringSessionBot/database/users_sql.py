from sqlalchemy import Column, BigInteger
from StringSessionBot.database import BASE, SESSION


class Users(BASE):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    user_id = Column(BigInteger, primary_key=True)

    def __init__(self, user_id, channels=None):
        self.user_id = user_id
        self.channels = channels

    # def __repr__(self):
    #     return "<User {} {} {} ({})>".format(self.thumbnail, self.thumbnail_status, self.video_to, self.user_id)


Users.__table__.create(checkfirst=True)


async def num_users():
    try:
        return SESSION.query(Users).count()
    finally:
        SESSION.close()
