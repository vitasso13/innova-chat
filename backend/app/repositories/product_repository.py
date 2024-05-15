
import sqlite3
from constants import DATABASE

class ProductRepository:
    def __init__(self):
        self.connection = sqlite3.connect(DATABASE)
        self.cursor = self.connection.cursor()

    def insert_product(self, id, name, description):
        self.cursor.execute('''
        INSERT INTO products (id, name, description) VALUES (?, ?, ?)
        ''', (id, name, description))
        self.connection.commit()

    def get_products_information(self):
        self.cursor.execute("SELECT * FROM products")
        products = self.cursor.fetchall()
        return products
    
    
    def initialize_database(self):
        self.cursor.execute('''
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

        self.cursor.executemany('''
        INSERT INTO products (id, name, description)
        VALUES (?, ?, ?)
        ''', products)

        self.connection.commit()
        self.connection.close()