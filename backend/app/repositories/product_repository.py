
import sqlite3
from os import environ
from app.migrations.product_migrations import products

DATABASE = environ.get('DATABASE', 'database.db')

class ProductRepository:
    def __init__(self):
        self.connection = sqlite3.connect(DATABASE)
        self.cursor = self.connection.cursor()

    def insert_product(self, id, name, description):
        self.cursor.execute('''
        INSERT INTO products (id, name, description) VALUES (?, ?, ?)
        ''', (id, name, description))
        self.connection.commit()
        self.connection.close()

    def get_products_information(self):
        self.cursor.execute("SELECT * FROM products")
        products = self.cursor.fetchall()
        self.connection.close()
        return products
    
    
    def initialize_database(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            features TEXT,
            use_cases TEXT,
            faq TEXT
        )
        ''')

        self.cursor.executemany('''
        INSERT INTO products (id, name, description, features, use_cases, faq)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', products)

        self.connection.commit()
        self.connection.close()