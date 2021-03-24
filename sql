import sqlite3



cn = sqlite3.connect()
cursor = cn.cursor()


def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS userss(name TEXT, password TEXT)")
    cn.commit()
def