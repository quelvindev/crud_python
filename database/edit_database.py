import sqlite3 as database
from database.connection_database import DATABASE_NAME



def edit_cargo(id):
    new_name = input('Digite o novo nome do cargo !')
    conn = database.connect(DATABASE_NAME)
    with conn:
        sql = conn.cursor()
        sql.execute("UPDATE cargo SET cargo = ? WHERE ID = ?", (new_name,id))
    conn.close()
    return

def edit_empresa(id):
    new_name = input('Digite o novo nome da empresa !')
    conn = database.connect(DATABASE_NAME)
    with conn:
        sql = conn.cursor()
        sql.execute("UPDATE empresa SET empresa = ? WHERE ID = ?", (new_name,id))
    conn.close()
    return

def edit_funcionario(id):
    new_name = input('Digite o novo nome do funcionario !')
    new_name2 = input('Digite o novo sobrenome do funcionario !')
    new_email = input('Digite o novo email do funcionario !')

    conn = database.connect(DATABASE_NAME)
    with conn:
        sql = conn.cursor()
        sql.execute("UPDATE funcionario SET nome = ?,sobrenome = ?, email = ? WHERE ID = ?", (new_name,new_name2,new_email,id))
    conn.close()
    return