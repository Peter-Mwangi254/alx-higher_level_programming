#!/usr/bin/python3

"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
This time the script is safe from
MySQL injections!
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    mycursor = db_conn.cursor()
    mycursor.execute("""SELECT * FROM states ORDER BY id ASC""")
    states_info = mycursor.fetchall()

    for state in states_info:
        if (state[1] == argv[4]):
            print(state)
