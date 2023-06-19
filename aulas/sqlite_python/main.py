import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME =   'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

#SQL

#CUIDADO: fazendo delete sem where

cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Criar a Tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}' 
    '('
        'id INTEGER PRIMARY KEY AUTOINCREMENT, '
        'name TEXT, '
        'weight REAL '
    ')'
)
connection.commit()

# Registrar valores na coluna da tabela
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(?, ?)'
)
# cursor.execute(sql, ['Gutierre', 85])
# cursor.executemany(
#     sql, 
#     (
#         ('Guthier', 10), 
#         ('Thiago', 85))
#     )
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:nome, :peso)'
)
# cursor.execute(sql, {'nome': 'Gutierre', 'peso': 85})
cursor.executemany(sql, [
    {'nome': 'Gutierre', 'peso': 85}, 
    {'nome': 'Guttemberg', 'peso': 20},
    {'nome': 'Guthier', 'peso': 9},
    {'nome': 'Gutim', 'peso': 20},
    ])

connection.commit()



if __name__ == '__main__':
    print(sql)
    cursor.execute(
        f'SELECT * FROM {TABLE_NAME}'
    )
        
    cursor.close()
    connection.close()
