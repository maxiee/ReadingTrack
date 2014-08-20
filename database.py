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
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        TITLE TEXT NOT NULL,
                        DATE FLOAT NOT NULL,
                        PAGECOUNT INT NOT NULL,
                        FINISHEDDATE FLOAT NOT NULL,
                        FINISHED INT NOT NULL,
                        RANK INT DEFAULT 0,
                        REVIEW TEXT DEFAULT "");''')

    def insert_a_book(self, title, page_count):
        self.conn.execute("INSERT INTO BOOK(TITLE, DATE, PAGECOUNT, FINISHEDDATE, FINISHED) VALUES (?, ?, ?, ?, ?)", 
                (title, time.time(), page_count, 0, 0))
        self.conn.commit()

    def remove_a_book(self, index):
        self.conn.execute("DELETE FROM BOOK WHERE rowid=?", (self.book_list[index][0], ))
        self.conn.commit()

    def finished_read(self, index, rank, review):
        self.conn.execute(
                "UPDATE BOOK SET FINISHED=1, FINISHEDDATE=?, RANK=?, REVIEW=? WHERE rowid=?", 
                (time.time(), rank, review, self.book_list[index][0], ))
        self.conn.commit()

    def get_books(self, finished):
        self.book_list = self.conn.execute("SELECT * FROM BOOK WHERE FINISHED=?", (finished, )).fetchall()
        return self.book_list

    def get_count(self):
        return len(self.book_list)
