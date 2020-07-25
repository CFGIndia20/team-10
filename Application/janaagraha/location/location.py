from geopy.geocoders import Nominatim


def location(address):
    geolocator = Nominatim(user_agent="Janaagraha")
    location = geolocator.geocode(address)
    return location.latitude, location.longitude



