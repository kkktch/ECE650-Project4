from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class T2(Base):
    __tablename__ = 't2'

    # emits SERIAL
    id = Column(Integer, primary_key=True)
    new_id = Column(Integer)


engine = create_engine(
    "postgresql://postgres:passw0rd@localhost:5432/ACC_BBALL", echo=True)
Base.metadata.create_all(engine)
