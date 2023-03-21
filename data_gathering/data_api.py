import requests

def geocode(address):
    params = { "q": address, 'format': 'json' }
    places = requests.get(f"https://nominatim.openstreetmap.org/search", params=params).json()

    return {'lat':float(places[0]['lat']),'lon':float(places[0]['lon'])}

def bikepoint_api(app_key):

    base_url = 'https://api.tfl.gov.uk/BikePoint'
    params_dict = {'app_key':app_key}

    res = requests.get(base_url,params_dict).json()

    return res
