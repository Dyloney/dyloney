import sqlite3

class Data():
    def __init__(self):
        self.conn = sqlite3.connect('data.db')
        self.c = self.conn.cursor()

        self.setup_tables()
        self.populate_categories()

    def setup_tables(self):
       c = self.c
       conn = self.conn

       c.execute('''CREATE TABLE if not exists items
                    (item_id integer, item_name text)''')

       c.execute('''CREATE TABLE if not exists current_items
                    (item_id integer, date text)''')

       c.execute('''CREATE TABLE if not exists deleted_items
                    (item_id integer, date text)''')

       c.execute('''CREATE TABLE if not exists item_categories
                    (item_id integer, category text)''')

    def populate_categories(self):
        '''
        Eventually query the server. Rebuild this list every
        time the program starts. Drop the table and restart.
        '''
        c = self.c
        categories = [
            ('Dairy',),
            ('Fish',),
            ('Meat',),
            ('Fruit',),
            ('Vegetable',),
            ('Frozen',),
            ('Grains',),
            ('Sweets',)
            ]

        c.execute('''DROP TABLE if exists categories''')

        c.execute('''CREATE TABLE categories
                     (category text)''')

        c.executemany('INSERT INTO categories VALUES (?)', categories)

    
