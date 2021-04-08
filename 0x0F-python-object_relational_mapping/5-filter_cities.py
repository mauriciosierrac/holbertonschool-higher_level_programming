#!/usr/bin/python3
'''module make join'''

from sys import argv
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2],
                           db=argv[3], charset="utf8")

    cur = conn.cursor()

    cur.execute("SELECT * FROM states JOIN cities\
        ON  states.id = cities.state_id ORDER BY cities.id ASC")

    query = cur.fetchall()
    x = ''
    for i in query:
        if i[1] == argv[4]:
            print('{}{}'.format(x, i[4]), end="")
            x = ', '
    print()

    cur.close()
    conn.close()
