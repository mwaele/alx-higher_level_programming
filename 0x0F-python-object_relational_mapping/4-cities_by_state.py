#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa
"""
if __name__ == '__main__':
    import MySQLdb
    import sys
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    v = '''SELECT cities.id, cities.name, states.name
           FROM states
           INNER JOIN cities
           ON states.id = cities.state_id
           ORDER BY cities.id'''
    cur.execute(v)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
