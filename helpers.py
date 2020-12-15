import sys
import pymssql

def get_db_connection():  # DB Connection
    #server = "192.168.43.177"
    server =  "192.168.68.110"   #myhome# virtual box IP
    database = 'master'
    username = 'SA'
    password = 'Root@sql'
    try:
        conn = pymssql.connect(server, username, password, database)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    return conn

