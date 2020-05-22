from kivymd.uix.dialog import ListMDDialog

"""
from kivy.uix.popup import Popup
from kivy.uix.label import Label
popup = Popup(title='Test popup', content=Label(text='Hello world'), size_hint=(None, None), size=(400, 400))
"""

class LocationPopupMenu(ListMDDialog):

    def __init__(self, location_data):
        super().__init__()
        # Info from csv file
        headers= "Lieu;X;Y;Description;Payant"
        headers= headers.split(';')
        print(location_data)
        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = location_data[i]
            setattr(self, attribute_name, attribute_value)
