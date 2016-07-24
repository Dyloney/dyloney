from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
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
foodlist.append(fooditem('Meat', 'Pork chops'))
foodlist.append(fooditem('Wheat/Grains', 'rolls'))
foodlist.append(fooditem('Fruit', 'pears'))
foodlist.append(fooditem('Vegetable', 'cucumber'))
foodlist.append(fooditem('Meat', 'bacon'))
foodlist.append(fooditem('Wheat/Grains', 'wheat'))
foodlist.append(fooditem('Fruit', 'orange'))
foodlist.append(fooditem('Vegetable', 'celery'))
foodlist.append(fooditem('Meat', 'beef'))
foodlist.append(fooditem('Wheat/Grains', 'white'))
foodlist.append(fooditem('Fruit', 'cantelope'))
foodlist.append(fooditem('Vegetable', 'tomato'))
foodlist.append(fooditem('Meat', 'hot dogs'))
foodlist.append(fooditem('Wheat/Grains', 'cake'))
foodlist.append(fooditem('Fruit', 'banana'))
foodlist.append(fooditem('Vegetable', 'onion'))
foodlist.append(fooditem('Meat', 'hamburger'))
foodlist.append(fooditem('Wheat/Grains', 'hotdog buns'))
foodlist.append(fooditem('Fruit', 'lemon'))
foodlist.append(fooditem('Vegetable', 'green beans'))
foodlist.append(fooditem('Meat', 'ribs'))
foodlist.append(fooditem('Wheat/Grains', 'french rolls'))
foodlist.append(fooditem('Miscellaneous', 'batteries'))
foodlist.append(fooditem('Dairy', 'milk'))
foodlist.append(fooditem('Dairy', 'eggs'))
foodlist.append(fooditem('Frozen Goods', 'tv dinners'))
foodlist.append(fooditem('Frozen Goods', 'hot Pockets'))

usedcat = {}


class POSFMApp(App):

    def build(self):
	layout = BoxLayout(orientation='vertical')
        self.tv = TreeView(root_options=dict(text='Tree One'), hide_root=True, indent_level=0, indent_start=0)
        self.tv.size_hint = 1, None
        self.tv.bind(minimum_height = self.tv.setter('height'))
        self.populate_tree_view(self.tv)

	self.menu = Button(text = 'Menu', size_hint =(1,.3))
        root = ScrollView(pos = (0, 0))
        root.add_widget(self.tv)
	layout.add_widget(root)
	layout.add_widget(self.menu)
	#root.add_widget(self.menu)
        return layout

    def populate_tree_view(self, tv):

        for i, item in enumerate(foodlist):
	    if item.categ not in usedcat.keys():
	        catbutton = TreeViewButton(text='%s' % item.categ, font_size = '50sp',
				size = (100, 450), background_color=[1,1,0,1])
	        catbutton.bind(on_press=self.cat_clicked)
                g = self.tv.add_node(catbutton)
		usedcat[item.categ] = g
	    else:
		g = usedcat[item.categ]
	    itembutton = TreeViewButton(text='%s' % item.name, font_size = '30sp',
				size = (100,150), background_color=[0,1,1,1])
	    itembutton.outline_height = 10
	    self.tv.add_node(itembutton, g)

    def cat_clicked(self, button):
        self.tv.toggle_node(button)

if __name__ == '__main__':
    POSFMApp().run()
