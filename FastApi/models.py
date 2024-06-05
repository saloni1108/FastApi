from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, create_engine
from sqlalchemy.orm import DeclarativeBase, declarative_base, sessionmaker
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

DB_URL =   "mysql+pymysql://root:AyeshA12345@localhost:3306/fast_practice"

engine = create_engine(url = DB_URL)

session = sessionmaker(bind = engine, autoflush = False, autocommit = False)

def get_db_session():
    db = session()
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"

    id:Mapped[int] = mapped_column(Integer, autoincrement = True, index = True, primary_key = True)
    name:Mapped[str] = mapped_column(String(length = 50))

# base = declarative_base()