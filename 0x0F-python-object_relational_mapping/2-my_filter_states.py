#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where name matches the argument
from the database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    
    db_conn = MySQLdb.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    mycursor = db_conn.cursor()

    mycursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
                        states.id ASC".format(argv[4]))
    rows_selected = mycursor.fetchall()

    for row in rows_selected:
        print(row)
