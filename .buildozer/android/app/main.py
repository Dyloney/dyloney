from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.treeview import TreeView, TreeViewNode
from kivy.uix.treeview import TreeViewLabel
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button

class TreeViewButton(Button, TreeViewNode):
    pass

class fooditem():
    def __init__(self, categ, name):
	self.categ = categ
	self.name = name

foodlist = []
foodlist.append(fooditem('Fruit', 'apple'))
foodlist.append(fooditem('Vegetable', 'carrots'))
foodlist.append(fooditem('Meat', 'Pork Chops'))
foodlist.append(fooditem('Bread', 'rolls'))
foodlist.append(fooditem('Fruit', 'apple'))
foodlist.append(fooditem('Vegetable', 'carrots'))
foodlist.append(fooditem('Meat', 'Pork Chops'))
foodlist.append(fooditem('Bread', 'rolls'))
foodlist.append(fooditem('Fruit', 'apple'))
foodlist.append(fooditem('Vegetable', 'carrots'))
foodlist.append(fooditem('Meat', 'Pork Chops'))
foodlist.append(fooditem('Bread', 'rolls'))
foodlist.append(fooditem('Fruit', 'apple'))
foodlist.append(fooditem('Vegetable', 'carrots'))
foodlist.append(fooditem('Meat', 'Pork Chops'))
foodlist.append(fooditem('Bread', 'rolls'))
foodlist.append(fooditem('Fruit', 'apple'))
foodlist.append(fooditem('Vegetable', 'carrots'))
foodlist.append(fooditem('Meat', 'Pork Chops'))
foodlist.append(fooditem('Bread', 'rolls'))
foodlist.append(fooditem('Fruit', 'apple'))
foodlist.append(fooditem('Vegetable', 'carrots'))
foodlist.append(fooditem('Meat', 'Pork Chops'))
foodlist.append(fooditem('Bread', 'rolls'))
usedcat = []

def populate_tree_view(tv):

    for i, item in enumerate(foodlist):
        g = tv.add_node(TreeViewLabel(text='%s' % item.categ, font_size = '50sp'))
        tv.add_node(TreeViewButton(text='%s' % item.name, font_size = '40sp'), g)

class POSFMApp(App):

    def build(self):
        tv = TreeView(root_options=dict(text='Tree One'), hide_root=True, indent_level=4)
        tv.size_hint = 1, None
        tv.bind(minimum_height = tv.setter('height'))
        populate_tree_view(tv)
        root = ScrollView(pos = (0, 0))
        root.add_widget(tv)
        return root

if __name__ == '__main__':
    POSFMApp().run()
