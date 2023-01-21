import sqlite3

class DBConnection:
    def __init__(self, parent = None):
        self.db = sqlite3.connect("user_accounts_data.db")
        self.cursor = self.db.cursor()
        self.cursor.execute(" CREATE TABLE IF NOT EXISTS user_account(account TEXT, password VARCHAR(255))")