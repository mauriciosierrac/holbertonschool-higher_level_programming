#!/usr/bin/python3
'''that module connect with my db'''
from sys import argv
import MySQLdb

if __name__ == '__main__':
    myUser = argv[1]
    myPswd = argv[2]
    myDb = argv[3]
    
    

conn = MySQLdb.connect(host="localhost", port=3306,
                       user=myUser, passwd="", db=myDb, charset="utf8")
cur = conn.cursor()

cur.execute("SELECT * FROM states WHERE name ='{myName}'".format(myName = argv[4]) )
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
