#!/usr/bin/python
__author__ = 'deepam'

import MySQLdb

try:
    db = MySQLdb.connect(host="localhost", user="ab", password="test", db="test")

    curs = db.cursor()

    curs.execute("select * from users")


    for row in curs.fetchall():
        print(" user: %s password: %s" % (row[1], row[2]))

except Exception as e:
    print(e)