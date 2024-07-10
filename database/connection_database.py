
import sqlite3 as database


DATABASE_NAME = 'database.db'


def start_connection():  
        
        try:
            conn = database.connect(DATABASE_NAME)
            print(f'{DATABASE_NAME} conectado com sucesso ...')
            sql = conn.cursor()
            sql.execute(f'CREATE TABLE IF NOT EXISTS cargo (id INTEGER PRIMARY KEY AUTOINCREMENT, cargo TEXT );')
            sql.execute(f'CREATE TABLE IF NOT EXISTS empresa (id INTEGER PRIMARY KEY AUTOINCREMENT, empresa TEXT )')
            sql.execute(f'CREATE TABLE IF NOT EXISTS funcionario (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, sobrenome TEXT, email TEXT )')
            
            
            
        except ConnectionError as e:
            print(f'Erro ao conectar o banco {DATABASE_NAME} erro: {e}')
            conn.close()



if __name__ == '__main__':
     start_connection()


   

