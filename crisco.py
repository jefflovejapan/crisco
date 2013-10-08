import base_62_converter as converter
import sqlite3


class shortener():

    def shorten(self, url):
        self.conn = sqlite3.connect('crisco_table.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS links
             (link text)''')
        self.c.execute("INSERT INTO links VALUES (?)", (url,))
        self.conn.commit()
        row_id = self.c.lastrowid
        return converter.dehydrate(row_id)

    def lengthen(self, input):
        self.conn = sqlite3.connect('crisco_table.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS links
             (link text)''')
        row_id = converter.saturate(input)
        self.c.execute("SELECT link FROM links WHERE rowid = ?",
                       (str(row_id),))
        url = self.c.fetchone()
        if url is not None:
            return url[0]
        else:
            return None
