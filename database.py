#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import sqlite3
import constants
import time

class Database():
    def __init__(self):
        self.book_list = []
        if os.path.isfile(constants.DB_NAME):
            print("Found database: " + constants.DB_NAME)
            self.conn = sqlite3.connect(constants.DB_NAME)
        else:
            print("Couldn't found database: " + constants.DB_NAME)
            print("Create a new one...")
            self.conn = sqlite3.connect(constants.DB_NAME)
            self.conn.execute('''CREATE TABLE BOOK
                        (TITLE TEXT NOT NULL,
                        DATE FLOAT NOT NULL,
                        PAGECOUNT INT NOT NULL,
                        FINISHED INT NOT NULL);''')

    def insert_a_book(self, title, page_count):
        self.conn.execute("INSERT INTO BOOK(TITLE, DATE, PAGECOUNT, FINISHED) VALUES (?, ?, ?, ?)", 
                (title, time.time(), page_count, 0))
        self.conn.commit()

    def get_books(self, finished):
        return self.conn.execute("SELECT * FROM BOOK WHERE FINISHED=?", (finished, )).fetchall()

    def get_count(self):
        return len(self.book_list)
