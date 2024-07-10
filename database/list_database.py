import sqlite3 as database
from database.connection_database import DATABASE_NAME
from models.cargo import Cargo
from models.empresa import Empresa
from models.funcionario import Funcionario


def list_cargo():
    conn = database.connect(DATABASE_NAME)
    lista = []
    with conn:
        sql = conn.cursor()
        sql.execute("SELECT id,cargo FROM cargo")
        valores = sql.fetchall()
        for id,cargo in valores:
            cargo = Cargo(id, cargo)
            lista.append(cargo)
    conn.close()

    for i in lista:
        print(i)
    return

def list_empresa():
    conn = database.connect(DATABASE_NAME)
    lista = []
    with conn:
        sql = conn.cursor()
        sql.execute("SELECT id,empresa FROM empresa")
        valores = sql.fetchall()
        for id,empresa in valores:
            empresa= Empresa(id, empresa)
            lista.append(empresa)
    conn.close()

    for i in lista:
        print(i)
    return


def list_funcionario():
    conn = database.connect(DATABASE_NAME)
    lista = []
    with conn:
        sql = conn.cursor()
        sql.execute("SELECT id,nome,sobrenome,email FROM funcionario")
        valores = sql.fetchall()
        for id,nome,sobrenome,email in valores:
            funcionario = Funcionario(id,nome,sobrenome,email)
            lista.append(funcionario)
    conn.close()

    for i in lista:
        print(i)
    return