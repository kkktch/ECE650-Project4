from sqlalchemy import create_engine, Column, Integer, String, Sequence, select
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


def query2(session, team_color):
    from main import Team, Color, State, Player
    team_names = session.query(Team).filter(
        Color.name == team_color, Team.color_id == Color.color_id)
    print("NAME")
    for single_name in team_names:
        print(single_name.name)


# engine = create_engine(
#     "postgresql://postgres:passw0rd@localhost:5432/ACC_BBALL")
# DBsession = sessionmaker(bind=engine)
# session = DBsession()

# query2(session, "Maroon")
