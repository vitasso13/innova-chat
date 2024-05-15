import sqlite3

DATABASE_URL = './database.db'

def get_product_information():
    connection = sqlite3.connect(DATABASE_URL)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    connection.close()
    return products


def initialize_database():
    connection = sqlite3.connect(DATABASE_URL)
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT NOT NULL
    )
    ''')

    products = [
        (1, 'Produto A', 'Descrição do Produto A...'),
        (2, 'Produto B', 'Descrição do Produto B...'),
        (3, 'Produto C', 'Descrição do Produto C...'),
    ]

    cursor.executemany('''
    INSERT INTO products (id, name, description)
    VALUES (?, ?, ?)
    ''', products)

    connection.commit()
    connection.close()
