from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.treeview import TreeView, TreeViewNode
from kivy.uix.treeview import TreeViewLabel
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown

from data import DataStore
from items import Item, NewItem

class TreeViewButton(Button, TreeViewNode):
    pass


class AddItemLayout(BoxLayout):
    def __init__(self, ds):
        super(AddItemLayout, self).__init__(orientation='vertical')
        self.name_input = TextInput()
        self.add_widget(self.name_input)
        self.submit = Button(text='Submit')
        self.add_widget(self.submit)
        self.ds = ds
        self.submit.bind(on_press=self.do_submit)
        
    def do_submit(self, button):
        name = self.name_input.text
        self.ds.insert_item(name)
        
usedcat = {}


class POSFMApp(App):

    def build(self):
	layout = FloatLayout()
        self.DataStore = DataStore()
        
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

        self.add.bind(on_press=self.add_clicked)
        
        return layout

    def populate_current_items(self):
        current_items = self.DataStore.get_current_item_ids()

        self.current_items_dict = {}
        for id in current_items:
            item = Item(self.DataStore, id)
            item.get_item_name()
            item.get_item_category()
            self.current_items_dict[id] = item

    def populate_tree_view(self, tv):

        self.populate_current_items()
            
        for i, item in self.current_items_dict.iteritems():
	    if item.category not in usedcat.keys():
	        catbutton = TreeViewButton(text='%s' % item.category, font_size = '50sp',
				size = (100, 450), background_color=[1,1,0,1])
	        catbutton.bind(on_press=self.cat_clicked)
                g = self.tv.add_node(catbutton)
		usedcat[item.category] = g
	    else:
		g = usedcat[item.category]
	    itembutton = TreeViewButton(text='%s' % item.name, font_size = '30sp',
				size = (100,150), background_color=[0,1,1,1])
	    itembutton.outline_height = 10
	    self.tv.add_node(itembutton, g)

    def cat_clicked(self, button):
        self.tv.toggle_node(button)

    def add_clicked(self, button):
        popup = Popup(title='Add Item',
                      content=AddItemLayout(self.DataStore),
                      size_hint=(None, None), size=(400, 400))

        popup.open()
        self.populate_tree_view(self.tv)
    


if __name__ == '__main__':
    POSFMApp().run()
