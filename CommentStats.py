#!/usr/bin/env python
# -*- coding: utf-8 -*-

SUBMISSIONID = "1ipkaj"
USERAGENT = "CommentStats"
USERNAME = "YourUserName"
PASSWORD = "YourPassword"

import praw
import sqlite3

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists

import os, sys

from dbobjects import Base, Dbcomment, Dbauthor


modbotpath = os.path.abspath(os.path.dirname(sys.argv[0]))
dblocation = os.path.join(modbotpath, SUBMISSIONID + ".db")

engine = create_engine("sqlite:///" + dblocation)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


print 'Start.'
r = praw.Reddit(user_agent=USERAGENT)
r.login(USERNAME, PASSWORD)
print 'Logged in'

commentlist = []

print "Getting data for: " , SUBMISSIONID

authorlist=set()

submission = r.get_submission(submission_id=SUBMISSIONID)
submission.replace_more_comments(limit=None)

flat_comments = praw.helpers.flatten_tree(submission.comments)

for comment in flat_comments:

    if isinstance(comment,praw.objects.MoreComments):
        print "Found MoreComments"
    else:
        if hasattr(comment,'author') and not comment.author == None:
            safeauthor = comment.author.name
            if comment.author.name not in authorlist:
                authorlist.add(comment.author.name)
        else:
            safeauthor = "[Deleted]"

        commententry = Dbcomment(id=comment.id, authorname = safeauthor, body = comment.body, ups = comment.ups,
                                 downs = comment.downs, parent_id = comment.parent_id, created_utc=comment.created_utc)
        commententry = session.merge(commententry)

        print comment.id, safeauthor, comment.ups, comment.downs

session.commit()

alreadylogged = session.query(Dbauthor)
for author in alreadylogged:
    if author.name in authorlist:
        authorlist.remove(author.name)

for currauthor in authorlist:
    author = r.get_redditor(currauthor)


    authorentry = Dbauthor(id=author.id, name = author.name, comment_karma = author.comment_karma,
                           link_karma = author.link_karma, is_gold = author.is_gold, created_utc=author.created_utc)
    session.merge(authorentry)

    print author.name, author.link_karma, author.comment_karma

session.commit()

print "Finished"

session.close()
