from kivy.garden.mapview import MapMarkerPopup
from locationpopupmenu import LocationPopupMenu


class LocationMarker(MapMarkerPopup):
    location_data = []

    def on_release(self):
        # Open up the LocationPopupMenu
        menu = LocationPopupMenu(self.location_data)
        menu.size_hint = [.8, .9]
        menu.open()
