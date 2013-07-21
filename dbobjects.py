# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Unicode, Float, String, BigInteger, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists

Base = declarative_base()



class Dbcomment(Base):
    __tablename__ = 'Comments'

    id = Column(Unicode, primary_key=True)
    authorname = Column(Unicode)
    body = Column(Unicode)
    ups = Column(BigInteger)
    downs = Column(BigInteger)
    parent_id = Column(Unicode)
    created_utc = Column(Float)


    def __init__(self, id, authorname, body, ups, downs, parent_id, created_utc):
        self.id = id
        self.authorname = authorname
        self.body = body
        self.ups = ups
        self.downs = downs
        self.parent_id = parent_id
        self.created_utc = created_utc

class Dbauthor(Base):
    __tablename__ = 'Authors'

    id = Column(Unicode, primary_key=True)
    name = Column(Unicode)
    comment_karma = Column(BigInteger)
    link_karma = Column(BigInteger)
    is_gold = Column(Unicode)
    created_utc = Column(Float)


    def __init__(self, id, name, comment_karma, link_karma, is_gold, created_utc):
        self.id= id
        self.name = name
        self.comment_karma = comment_karma
        self.link_karma = link_karma
        self.is_gold = is_gold
        self.created_utc = created_utc

