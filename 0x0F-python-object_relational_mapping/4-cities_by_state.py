#!/usr/bin/python3
"""
This script lists all cities from
the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    

    db_conn = MySQLdb.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    mycursor = db_conn.cursor()
    mycursor.execute("SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")
    rows_selected = mycursor.fetchall()

    if rows_selected is not None:
        for row in rows_selected:
            print(row)
