from sqlalchemy import create_engine, Column, Integer, String, Sequence, select
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy.orm.session.Session as Session
import os
import main


def query2(Session session, string team_color):
    team_names = session.query(Team).filter(
        Color.name == "Red", Team.color_id == Color.color_id)
    print("NAME")
    for single_name in team_names:
        print(single_name.name)
