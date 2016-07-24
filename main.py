from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
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
    def __init__(self, item):
	self.categ = item[0]
	self.name = item[1]

foodlist = []
with open('data/testdata.txt') as f:
    for i in f:
	i = i.strip('\n')
	datum = tuple(map(str, i.split(',')))
	foodlist.append(fooditem(datum))

usedcat = {}


class POSFMApp(App):

    def build(self):
	layout = FloatLayout()
        self.tv = TreeView(root_options=dict(text='Tree One'), hide_root=True, indent_level=0, indent_start=0)
        self.tv.size_hint = 1, None
        self.tv.bind(minimum_height = self.tv.setter('height'))
        self.populate_tree_view(self.tv)

	self.camera = Button(text = 'Camera', size_hint =(1/3.,.23),
				background_color=[1,0,0,.6], pos_hint={'x':0,'y':0})
	self.add = Button(text = 'Add', size_hint =(1/3.,.23),
			background_color=[1,0,0,.6], pos_hint={'x':1/3.,'y':0})
	self.sort = Button(text = 'Sort', size_hint =(1/3.,.23), 
			   background_color=[1,0,0,.6], pos_hint={'x':2/3.,'y':0})
        root = ScrollView(pos = (0, 0))
        root.add_widget(self.tv)
	layout.add_widget(root)
	layout.add_widget(self.camera)
	layout.add_widget(self.add)
	layout.add_widget(self.sort)
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
