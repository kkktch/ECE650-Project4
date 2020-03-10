from sqlalchemy import create_engine, Column, Integer, String, Sequence, select
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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


def query2(session, team_color):
    team_names = session.query(Team).filter(
        Color.name == team_color, Team.color_id == Color.color_id)
    print("NAME")
    for single_name in team_names:
        print(single_name.name)


def query3(session, team_name):
    p_names = session.query(Player).filter(
        Player.team_id == Team.team_id, Team.name == team_name).order_by(Player.ppg.desc())
    print("FIRST_NAME LAST_NAME")
    for single_player in p_names:
        print(single_player.first_name, " ", single_player.last_name)


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
    new_color = Color(name=line_list[1])
    session.add(new_color)
    session.commit()
color_file.close()

state_file = open("state.txt")
state_lines = state_file.readlines()
for line in state_lines:
    line_list = line.split()
    new_state = State(name=line_list[1])
    session.add(new_state)
    session.commit()
state_file.close()

team_file = open("team.txt")
team_lines = team_file.readlines()
for line in team_lines:
    line_list = line.split()
    new_team = Team(name=line_list[1], state_id=int(line_list[2]),
                    color_id=int(line_list[3]), wins=int(line_list[4]), losses=int(line_list[5]))
    session.add(new_team)
    session.commit()
team_file.close()

player_file = open("player.txt")
player_lines = player_file.readlines()
for line in player_lines:
    line_list = line.split()
    new_player = Player(team_id=int(line_list[1]), uniform_num=int(line_list[2]), first_name=line_list[3], last_name=line_list[4], mpg=int(
        line_list[5]), ppg=int(line_list[6]), rpg=int(line_list[7]), apg=int(line_list[8]), spg=float(line_list[9]), bpg=float(line_list[10]))
    session.add(new_player)
    session.commit()
player_file.close()

query2(session, "Red")
query3(session, "GeorgiaTech")

session.close()
