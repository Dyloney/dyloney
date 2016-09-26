import sqlite3
import time
import os
from errors import *

class DataStore():
    def __init__(self):
        self.conn =  sqlite3.connect(os.path.expanduser('~/Documents/data.db'))
        #self.conn = sqlite3.connect('data.db')
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
                    (item_id integer, date_inserted text, date_deleted text)''')

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
            ('Produce',),
            ('Frozen',),
            ('Grains',),
            ('Sweets',)
            ]

        c.execute('''DROP TABLE if exists categories''')

        c.execute('''CREATE TABLE categories
                     (category text)''')

        c.executemany('INSERT INTO categories VALUES (?)', categories)
        c.connection.commit()

    def get_categories(self):
        '''
        Get all the available categories from the database
        '''

        c = self.c
        c.execute('SELECT category FROM categories''')
        categories = c.fetchall()
        categories = [str(cat[0]) for cat in categories]
        return categories

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

        date = (time.strftime("%d/%m/%Y"))

        c.execute('INSERT INTO current_items VALUES (?, ?)', (item_id, date))
        c.connection.commit()
        return item_id

    def assign_category(self, item_id, category):
        '''
        Assign a category to an item
        '''

        c = self.c
        c.execute('INSERT INTO item_categories VALUES (?, ?)', (item_id, category))
        c.connection.commit()

    def delete_item(self, item_id):
        '''
        Remove item_id from the current_items table.
        Add item_id to the deleted_items table.
        '''

        c = self.c
        date_deleted = (time.strftime("%d/%m/%Y"))
        c.execute('SELECT date FROM current_items WHERE item_id = ?', (item_id, ))
        date_inserted = str(c.fetchone()[0])
        c.execute('DELETE FROM current_items WHERE item_id = ?', (item_id, ))
        c.execute('INSERT INTO deleted_items VALUES (?, ?, ?)', (item_id, date_inserted, date_deleted))
        c.connection.commit()

    def get_current_item_ids(self):
        '''
        Return all current item_ids
        '''
        c = self.c
        item_ids = [row[0] for row in c.execute('SELECT item_id from current_items')]
        return item_ids

    def get_item_name(self, item_id):
        '''
        Return name of item with the specified item_id
        '''

        c = self.c
        c.execute('SELECT item_name FROM items WHERE item_id = ?', (item_id, ))
        name = str(c.fetchone()[0])
        return name

    def get_item_category(self, item_id):
        '''
        Return the category of item with the specified item_id
        '''

        c = self.c
        c.execute('SELECT category from item_categories WHERE item_id = ?', (item_id, ))
        try:
            category = str(c.fetchone()[0])
            return category
        except TypeError:
            raise ItemNotFoundException('Category not defined')

    def get_item_date_inserted(self, item_id):
        c = self.c
        c.execute('SELECT date FROM current_items WHERE item_id = ?', (item_id, ))
        date = str(c.fetchone()[0])
        if date is None: # check the deleted items
            c.execute('SELECT date_inserted FROM deleted_items WHERE item_id = ?', (item_id, ))
            date = str(c.fetchone()[0])
        if date is not None:
            return date
        else:
            raise ItemNotFoundException('No such item')
