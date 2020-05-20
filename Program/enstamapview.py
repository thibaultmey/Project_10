from kivy.garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from kivy.garden.mapview import MapMarkerPopup

class LocationMarker(MapMarkerPopup):
    location_data = []

class EnstaMapView(MapView):
    getting_locations_timer = None
    location_names = []

    def start_getting_locations_in_fov(self):
        # After one second update all locations in fov
        try:
            self.getting_locations_timer.cancel()
        except:
            pass

        self.getting_locations_timer = Clock.schedule_once(self.get_locations_in_fov, 1)

    def get_locations_in_fov(self, *args):
        min_x, min_y, max_x, max_y = self.get_bbox()
        app = App.get_running_app()
        app.cursor = app.connection.cursor()
        app.cursor.execute("SELECT * FROM locations WHERE X>(?) AND X<(?) AND Y>(?) AND Y<(?)",(min_x,max_x,min_y,max_y))
        locations = app.cursor.fetchall()
        print(locations)
        for location in locations:
            name = location[0]
            if name in self.location_names:
                continue
            self.add_location(location)

    def add_location(self, location):
        #Create the location marker
        x, y = location[1], location[2]
        marker = LocationMarker(lat=x, lon=y)
        marker.location_data = location
        #add the marker to the map
        self.add_widget(marker)
        #Keep track of the marker's name so we don't put two markers on the same spot
        name = location[0]
        self.location_names.append(name)