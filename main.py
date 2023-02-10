import pymysql

conn = pymysql.connect(host="localhost", user="root",password="",db="python_db")
myCursor=conn.cursor()

myCursor.excecute()