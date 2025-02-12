from sqlalchemy import create_engine, Column, Integer, String, Sequence, select
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from query_funcs import query1, query2, query3, query4, query5, add_color, add_player, add_state, add_team
import os


def exercise():
    engine = create_engine(
        "postgresql://postgres:passw0rd@localhost:5432/ACC_BBALL")
    DBsession = sessionmaker(bind=engine)
    session = DBsession()

    add_state(session, "test_state")
    add_color(session, "test_color")
    add_team(session, "test_team", 0, 0, 0, 0)
    query1(session, 1, 10, 38, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    query1(session, 0, 10, 38, 1, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    query1(session, 0, 10, 38, 0, 0, 20, 1, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    query1(session, 0, 10, 38, 0, 0, 20, 0, 0, 5, 1, 0, 5, 0, 0, 0, 0, 0, 0)
    query1(session, 0, 10, 38, 0, 0, 20, 0, 0, 5, 0, 0, 5, 1, 0, 5, 0, 0, 0)
    query1(session, 0, 10, 38, 0, 0, 20, 0, 0, 5, 0, 0, 5, 0, 0, 5, 1, 0, 5)
    query1(session, 0, 10, 38, 1, 0, 20, 0, 0, 5, 0, 0, 5, 0, 0, 5, 1, 0, 5)
    query1(session, 0, 10, 38, 0, 0, 20, 1, 0, 5, 0, 0, 5, 1, 0, 5, 1, 0, 5)
    add_player(session, 1, 1, "first_test", "last_test", 0, 0, 0, 0, 0, 3)
    query1(session, 0, 10, 38, 0, 0, 20, 1, 0, 5, 0, 0, 5, 1, 0, 5, 1, 0, 5)
    query1(session, 1, 10, 38, 1, 0, 20, 1, 0, 5, 1, 0, 5, 1, 0, 5, 1, 0, 5)
    query2(session, "Gold")
    query2(session, "Red")
    query2(session, "Green")
    query2(session, "NoExist")
    query3(session, "GeorgiaTech")
    query3(session, "NoExist")
    query4(session, "FL", "Gold")
    query4(session, "NC", "DarkBlue")
    query5(session, 12)
    query5(session, 10)
    query5(session, 50)
    return
