from sqlalchemy import create_engine, Column, Integer, String, Sequence, select
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from main import State, Team, Color, Player
import os


def add_player(session, team_id_in, jersey_num, first_name_in, last_name_in,
               mpg_in, ppg_in, rpg_in, apg_in, spg_in, bpg_in):
    new_player = Player(team_id=int(team_id_in), uniform_num=int(jersey_num), first_name=first_name_in, last_name=last_name_in, mpg=int(
        mpg_in), ppg=int(ppg_in), rpg=int(rpg_in), apg=int(apg_in), spg=float(spg_in), bpg=float(bpg_in))
    session.add(new_player)
    session.commit()


def add_team(session, name_in, state_id_in, color_id_in, wins_in, losses_in):
    new_team = Team(name=name_in, state_id=int(state_id_in),
                    color_id=int(color_id_in), wins=int(wins_in), losses=int(losses_in))
    session.add(new_team)
    session.commit()


def add_color(session, name_in):
    new_color = Color(name=name_in)
    session.add(new_color)
    session.commit()


def add_state(session, name_in):
    new_state = State(name=name_in)
    session.add(new_state)
    session.commit()


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
