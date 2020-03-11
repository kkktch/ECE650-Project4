from sqlalchemy import create_engine, Column, Integer, String, Sequence, select
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import query_funcs
import os


def exercise():
    engine = create_engine(
        "postgresql://postgres:passw0rd@localhost:5432/ACC_BBALL")
    DBsession = sessionmaker(bind=engine)
    session = DBsession()

    query_funcs.query1(session, 1, 10, 38, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    query_funcs.query1(session, 0, 10, 38, 1, 0, 20, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    query_funcs.query1(session, 0, 10, 38, 0, 0, 20, 1,
                       0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    query_funcs.query1(session, 0, 10, 38, 0, 0, 20, 0,
                       0, 5, 1, 0, 5, 0, 0, 0, 0, 0, 0)
    query_funcs.query1(session, 0, 10, 38, 0, 0, 20, 0,
                       0, 5, 0, 0, 5, 1, 0, 5, 0, 0, 0)
    query_funcs.query1(session, 0, 10, 38, 0, 0, 20, 0,
                       0, 5, 0, 0, 5, 0, 0, 5, 1, 0, 5)
    query_funcs.query1(session, 0, 10, 38, 1, 0, 20, 0,
                       0, 5, 0, 0, 5, 0, 0, 5, 1, 0, 5)
    query_funcs.query1(session, 0, 10, 38, 0, 0, 20, 1,
                       0, 5, 0, 0, 5, 1, 0, 5, 1, 0, 5)
    query_funcs.query1(session, 1, 10, 38, 1, 0, 20, 1,
                       0, 5, 1, 0, 5, 1, 0, 5, 1, 0, 5)
    query_funcs.query2(session, "Gold")
    query_funcs.query2(session, "Red")
    query_funcs.query2(session, "NoExist")
    query_funcs.query3(session, "GeorgiaTech")
    query_funcs.query3(session, "NoExist")
    query_funcs.query4(session, "FL", "Gold")
    query_funcs.query4(session, "NC", "DarkBlue")
    query_funcs.query5(session, 12)
    query_funcs.query5(session, 10)
    query_funcs.query5(session, 50)
