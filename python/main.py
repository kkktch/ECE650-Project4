from sqlalchemy import create_engine, Column, Integer, String, Sequence, DOUBLE_PRECISION
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


class Team(Base):
    __tablename__ = 'team'

    team_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(256))
    state_id = Column(Integer, ForeignKey("state.state_id"))
    color_id = Column(Integer, ForeignKey("color.color_id"))
    wins = Column(Integer)
    losses = Column(Integer)


class Player(Base):
    __tablename__ = 'player'

    player_id = Column(Integer, autoincrement=True, primary_key=True)
    team_id = Column(Integer, ForeignKey("team.team_id"))
    uniform_num = Column(Integer)
    first_name = Column(String(256))
    last_name = Column(String(256))
    mpg = Column(Integer)
    ppg = Column(Integer)
    rpg = Column(Integer)
    apg = Column(Integer)
    spg = Column(DOUBLE_PRECISION)
    bpg = Column(DOUBLE_PRECISION)


engine = create_engine(
    "postgresql://postgres:passw0rd@localhost:5432/ACC_BBALL", echo=True)
Player.__table__.drop(engine, checkfirst=True)
Team.__table__.drop(engine, checkfirst=True)
State.__table__.drop(engine, checkfirst=True)
Color.__table__.drop(engine, checkfirst=True)
Base.metadata.create_all(engine)
