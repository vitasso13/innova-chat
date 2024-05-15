
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