#!/usr/bin/python3
'''that module connect with my DB'''

from sys import argv
import MySQLdb

if __name__ == '__main__':

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[0], passwd=argv[1],
                           db=argv[2], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
