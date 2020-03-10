from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'state'

    state_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(256))


class Color(Base):
    __tablename__ = 'color'

    color_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(256))


Re_Engine = create_engine(
    "postgresql://postgres:passw0rd@localhost:5432/postgres")
conn = Re_Engine.connect()
conn.execute("commit")
conn.execute("drop database if exists \"ACC_BBALL\"")
conn.execute("create database \"ACC_BBALL\"")
conn.close()

engine = create_engine(
    "postgresql://postgres:passw0rd@localhost:5432/ACC_BBALL", echo=True)
State.__table__.drop(engine, checkfirst=True)
Color.__table__.drop(engine, checkfirst=True)
Base.metadata.create_all(engine)
