import sqlite3 as sq


class DatabaseManager:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def create_table_levels(self):
        with sq.connect(self.db_path) as conn:
            conn.execute(
                """CREATE TABLE IF NOT EXISTS orders_buy (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    order_price REAL NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )"""
            )
            conn.execute(
                """CREATE TABLE IF NOT EXISTS orders_sell (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    order_price REAL NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )"""
            )

    def add_order_buy(self, order):
        pass

    def add_order_sell(self, order):
        pass
