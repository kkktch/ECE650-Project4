from sqlalchemy import create_engine, Column, Integer, String, Sequence, select
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from query_funcs import add_color, add_player, add_state, add_team
from exercise import exercise
import os

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
    state_id = Column(Integer)
    color_id = Column(Integer)
    wins = Column(Integer)
    losses = Column(Integer)


class Player(Base):
    __tablename__ = 'player'

    player_id = Column(Integer, autoincrement=True, primary_key=True)
    team_id = Column(Integer)
    uniform_num = Column(Integer)
    first_name = Column(String(256))
    last_name = Column(String(256))
    mpg = Column(Integer)
    ppg = Column(Integer)
    rpg = Column(Integer)
    apg = Column(Integer)
    spg = Column(DOUBLE_PRECISION)
    bpg = Column(DOUBLE_PRECISION)


def main():
    engine = create_engine(
        "postgresql://postgres:passw0rd@localhost:5432/ACC_BBALL")
    Player.__table__.drop(engine, checkfirst=True)
    Team.__table__.drop(engine, checkfirst=True)
    State.__table__.drop(engine, checkfirst=True)
    Color.__table__.drop(engine, checkfirst=True)
    Base.metadata.create_all(engine)

    DBsession = sessionmaker(bind=engine)
    session = DBsession()

    color_file = open("color.txt")
    color_lines = color_file.readlines()
    for line in color_lines:
        line_list = line.split()
        add_color(session, line_list[1])
    color_file.close()

    state_file = open("state.txt")
    state_lines = state_file.readlines()
    for line in state_lines:
        line_list = line.split()
        add_state(session, line_list[1])
    state_file.close()

    team_file = open("team.txt")
    team_lines = team_file.readlines()
    for line in team_lines:
        line_list = line.split()
        add_team(session, line_list[1], line_list[2],
                 line_list[3], line_list[4], line_list[5])
    team_file.close()

    player_file = open("player.txt")
    player_lines = player_file.readlines()
    for line in player_lines:
        line_list = line.split()
        add_player(session, line_list[1], line_list[2], line_list[3], line_list[4],
                   line_list[5], line_list[6], line_list[7], line_list[8], line_list[9], line_list[10])
    player_file.close()
    session.close()

    exercise()


if __name__ == "__main__":
    main()
