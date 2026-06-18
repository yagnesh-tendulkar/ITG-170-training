import pymysql



def get_connection():

    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="M1racle@123",
        database="company_db",
        cursorclass=pymysql.cursors.DictCursor
    )

    return connection