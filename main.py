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


class POSFMApp(App):

    def build(self):
        self.tv = TreeView(root_options=dict(text='Tree One'), hide_root=True, indent_level=0, indent_start=0)
        self.tv.size_hint = 1, None
        self.tv.bind(minimum_height = self.tv.setter('height'))
        self.populate_tree_view(self.tv)
        root = ScrollView(pos = (0, 0))
        root.add_widget(self.tv)
        return root

    def populate_tree_view(self, tv):

        for i, item in enumerate(foodlist):
	    catbutton = TreeViewButton(text='%s' % item.categ, font_size = '50sp', background_color=[1,1,0,1])
	    catbutton.bind(on_press=self.cat_clicked)
            g = self.tv.add_node(catbutton)
            self.tv.add_node(TreeViewButton(text='%s' % item.name, font_size = '40sp'), g)

    def cat_clicked(self, button):
        self.tv.toggle_node(button)

if __name__ == '__main__':
    POSFMApp().run()
