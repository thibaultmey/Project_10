from kivymd.app import MDApp
from enstamapview import EnstaMapView
import sqlite3
import pandas
from searchpopupmenu import SearchPopupMenu

class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None

    def on_start(self):
        # Connect to database
        self.connection = sqlite3.connect("locations.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS locations(Lieu TEXT,X REAL,Y REAL,Description TEXT,Payant TEXT,PRIMARY KEY(Lieu,X,Y,Description,Payant))''')
        try:
            df = pandas.read_csv('locations.csv')
            df.to_sql('locations', self.connection, if_exists='append', index=False)
        except:
            pass
        self.connection.commit()

        #search pop up menu:
        self.search_menu = SearchPopupMenu()


MainApp().run()
