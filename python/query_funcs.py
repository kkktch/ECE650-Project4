from sqlalchemy import create_engine, Column, Integer, String, Sequence, select
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


# engine = create_engine(
#     "postgresql://postgres:passw0rd@localhost:5432/ACC_BBALL")
# DBsession = sessionmaker(bind=engine)
# session = DBsession()

# query2(session, "Maroon")
