import sqlite3 as database
from database.connection_database import DATABASE_NAME



def delete_cargo(id):
    
    conn = database.connect(DATABASE_NAME)
    with conn:
        sql = conn.cursor()
        sql.execute("DELETE FROM cargo WHERE ID = ?", (id))
    conn.close()
    return


def delete_empresa(id):
    
    conn = database.connect(DATABASE_NAME)
    with conn:
        sql = conn.cursor()
        sql.execute("DELETE FROM empresa WHERE ID = ?", (id))
    conn.close()
    return

def delete_funcionario(id):
    
    conn = database.connect(DATABASE_NAME)
    with conn:
        sql = conn.cursor()
        sql.execute("DELETE FROM funcionario WHERE ID = ?", (id))
    conn.close()
    return