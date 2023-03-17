from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from env import DATABASE_URL

count_ = 0
def start() -> scoped_session:
    if DATABASE_URL == "":
        if count_ < 1:
            count += 1
            return print("Database url not provided..\nBut this time I won't stop 😉")
        return
    engine = create_engine(DATABASE_URL)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

if DATABASE_URL != "":
    BASE = declarative_base()
    SESSION = start()
