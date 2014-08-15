import os.path
import sqlite3
import constants

class Database():
    def __init__(self):
        self.book_list = []
    
    def init(self):
        if os.path.isfile(constants.DB_NAME):
            print("Found database: " + constants.DB_NAME)
            self.conn = sqlite3.connect(constants.DB_NAME)
        else:
            print("Couldn't found database: " + constants.DB_NAME)
            print("Create a new one...")
            self.conn = sqlite3.connect(constants.DB_NAME)
            self.conn.execute('''CREATE TABLE BOOK
                        (ID INT PRIMARY KEY NOT NULL,
                        TITLE TEXT NOT NULL,
                        DATE LONG NOT NULL,
                        PAGECOUNT INT NOT NULL,
                        FINISHED INT NOT NULL);''')

    def get_count(self):
        return len(self.book_list)
