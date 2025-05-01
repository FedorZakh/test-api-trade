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
                    quantity REAL NOT NULL,
                    order_price REAL NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )"""
            )
            conn.execute(
                """CREATE TABLE IF NOT EXISTS orders_sell (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    quantity REAL NOT NULL,
                    order_price REAL NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )"""
            )

    def add_order_buy(self, name: str, quantity: float, order_price: float):
        """Добавляет ордер покупки"""
        with sq.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO orders_buy (name, quantity, order_price ) VALUES (?, ?, ?)",
                (
                    name,
                    quantity,
                    order_price,
                ),
            )

    def add_order_sell(self, name: str, quantity: float, order_price: float):
        """Добавляет ордер продажи"""
        with sq.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO orders_sell (name, quantity, order_price) VALUES (?, ?, ?)",
                (
                    name,
                    quantity,
                    order_price,
                ),
            )
