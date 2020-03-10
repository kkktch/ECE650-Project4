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


def query1(session, use_mpg, min_mpg, max_mpg,
           use_ppg, min_ppg, max_ppg,
           use_rpg, min_rpg, max_rpg,
           use_apg, min_apg, max_apg,
           use_spg, min_spg, max_spg,
           use_bpg, min_bpg, max_bpg):
    tmp = session.query(Player)
    if (use_mpg):
        tmp = tmp.filter(Player.mpg >= min_mpg, Player.mpg <= max_mpg)
    if (use_ppg):
        tmp = tmp.filter(Player.ppg >= min_ppg, Player.ppg <= max_ppg)
    if (use_rpg):
        tmp = tmp.filter(Player.rpg >= min_rpg, Player.rpg <= max_rpg)
    if (use_apg):
        tmp = tmp.filter(Player.apg >= min_apg, Player.apg <= max_apg)
    if (use_spg):
        tmp = tmp.filter(Player.spg >= min_spg, Player.spg <= max_spg)
    if (use_bpg):
        tmp = tmp.filter(Player.bpg >= min_bpg, Player.bpg <= max_bpg)

    print("PLAYER_ID TEAM_ID UNIFORM_NUM FIRST_NAME LAST_NAME MPG PPG RPG APG SPG BPG")
    for single_player in tmp:
        print(str(single_player.player_id) + " " + str(single_player.team_id) + " " + str(single_player.uniform_num) + " " + single_player.first_name + " " + single_player.last_name + " " +
              str(single_player.mpg) + " " + str(single_player.ppg) + " " + str(single_player.rpg) + " " + str(single_player.apg) + " " + str('%.1f' % single_player.spg) + " " + str('%.1f' % single_player.bpg))


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
        print(single_player.first_name + " " + single_player.last_name)


def query4(session, team_state, team_color):
    nms = session.query(Player).filter(
        Player.team_id == Team.team_id, Team.color_id == Color.color_id,
        Team.state_id == State.state_id, State.name == team_state, Color.name == team_color)
    print("FIRST_NAME LAST_NAME UNIFORM_NUM")
    for single_nm in nms:
        print(single_nm.first_name + " " +
              single_nm.last_name + " " + str(single_nm.uniform_num))


def query5(session, num_wins):
    win_p = session.query(Player, Team).filter(
        Player.team_id == Team.team_id, Team.wins > num_wins)
    print("FIRST_NAME LAST_NAME TEAM_NAME WINS")
    for single_win in win_p:
        print(single_win[0].first_name + " " + single_win[0].last_name + " " +
              single_win[1].name + " " + str(single_win[1].wins))


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

query1(session, 1, 35, 40, 0, 0, 0, 0, 5, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0)
query1(session, 0, 35, 40, 0, 0, 0, 1, 5, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0)
query1(session, 0, 35, 40, 1, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
query1(session, 0, 35, 40, 0, 0, 0, 0, 0, 0, 1, 0, 10, 0, 0, 0, 0, 0, 0)
query1(session, 0, 35, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 5, 0, 0, 0)
query1(session, 0, 35, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 5)
query2(session, "Gold")
query2(session, "NoExist")
query3(session, "GeorgiaTech")
query3(session, "NoExist")
query4(session, "FL", "Gold")
query4(session, "NC", "DarkBlue")
query5(session, 12)

session.close()
