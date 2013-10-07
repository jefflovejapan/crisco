#!/usr/bin/python

import base_62_converter as converter
import sqlite3


class shortener():

    def __init__(self):
        self.conn = sqlite3.connect('crisco_table.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS links
             (link text)''')
        print 'This works'

    def shorten(self, url):
        self.c.execute("INSERT INTO links VALUES (?)", (url,))
        self.conn.commit()
        row_id = self.c.lastrowid
        return converter.dehydrate(row_id)

    def lengthen(self, input):
        row_id = converter.saturate(input)
        self.c.execute("SELECT link FROM links WHERE rowid = ?",
                       (str(row_id),))
        url = self.c.fetchone()
        return url[0]
