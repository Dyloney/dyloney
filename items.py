'''
Classes for various items
'''

from errors import *

class Item():
    def __init__(self, ds, item_id):
        '''
        ds = DataStore
        item_id = unique id for this item
        '''

        self.ds = ds
        self.item_id = item_id

    def get_item_name(self):
        self.name = self.ds.get_item_name(self.item_id)
        return self.name

    def get_item_category(self):
        try:
            self.category = self.ds.get_item_category(self.item_id)
        except ItemNotFoundException:
            self.category = "None"
        return self.category


class NewItem():
    def __init__(self, ds, name):
        self.ds = ds
        self.item_id = self.ds.insert_item(name)

    def set_category(self, category):
        self.ds.assign_category(self.item_id, category)

    
