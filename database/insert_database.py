import sqlite3 as database
from database.connection_database import DATABASE_NAME
from models.cargo import Cargo
from models.empresa import Empresa
from models.funcionario import Funcionario





def insert_cargo(nome):
    conn = database.connect(DATABASE_NAME)
    with conn:
        sql = conn.cursor()
        sql.execute("INSERT INTO cargo (cargo) VALUES ( ?)", (nome,))
    conn.close()
    return

def insert_empresa(nome):
    conn = database.connect(DATABASE_NAME)
    with conn:
        sql = conn.cursor()
        sql.execute("INSERT INTO empresa (empresa) VALUES ( ?)", (nome,))
    conn.close()
    return

def insert_funcionario(funcionario:Funcionario):
    conn = database.connect(DATABASE_NAME)
    with conn:
        sql = conn.cursor()
        sql.execute("INSERT INTO funcionario (nome,sobrenome,email) VALUES ( ?,?,?)", (funcionario.nome,funcionario.sobremome,funcionario.emal))
    conn.close()
    return





