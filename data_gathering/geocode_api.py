import requests

def geocode(address):
    params = { "q": address, 'format': 'json' }
    places = requests.get(f"https://nominatim.openstreetmap.org/search", params=params).json()

    return {'lat':float(places[0]['lat']),'lon':float(places[0]['lon'])}
