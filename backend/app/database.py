import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Criando tabela de produtos
cursor.execute('''
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL
)
''')

# Inserindo dados de exemplo
products = [
    (1, 'Produto A', 'Descrição do Produto A...'),
    (2, 'Produto B', 'Descrição do Produto B...'),
    (3, 'Produto C', 'Descrição do Produto C...'),
]

cursor.executemany('''
INSERT INTO products (id, name, description) VALUES (?, ?, ?)
''', products)

connection.commit()
connection.close()