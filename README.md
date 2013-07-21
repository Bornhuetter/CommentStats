CommentStats
============

Script for pulling all of the comments from a reddit submission into a database, along with some stats on the authors of the comments.

The name of the database generated will be the same as the name of the submission ID.

You must change the submission ID, username and password in the source code in order for this to work.

This script requires

* Python 2.7
* PRAW
* Sqlalchemy
* Sqlite

You can install PRAW and Sqlalchemy using pip, and sqlite using apt-get on Debian based systems (eg Ubuntu).

pm me at /u/bornhuetter if you need any help setting this up.
