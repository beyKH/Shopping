import sqlite3

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS userlar(login TEXT, password TEXT)")
    cn.commit()


def add_user():
    sql = "INSERT INTO userlar VALUES(?,?)"
    us_login = input("please enter login: ")
    us_password = input("please enter password: ")
    cursor.execute(sql, (us_login, us_password))
    cn.commit()

cn = sqlite3.connect("D:\exam prep/data.db")
cursor = cn.cursor()



create_table()
add_user()