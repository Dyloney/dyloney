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
                    (item_id integer primary key, item_name text)''')

       c.execute('''CREATE TABLE if not exists current_items
                    (item_id integer, date text)''')

       c.execute('''CREATE TABLE if not exists deleted_items
                    (item_id integer, date text)''')

       c.execute('''CREATE TABLE if not exists item_categories
                    (item_id integer, category text)''')

       c.connection.commit()

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
        c.connection.commit()

    def insert_item(self, name):
        '''
        Insert an item into the database.
        Add the item_id to the current_items table.
        Does not assign a category.
        Returns item_id.
        '''

        c = self.c
        c.execute('INSERT INTO items(item_name) VALUES (?)', (name, ))
        item_id = c.lastrowid

        c.execute('INSERT INTO current_items VALUES (?, ?)', (item_id, name))
        c.connection.commit()
        return item_id

        
        
