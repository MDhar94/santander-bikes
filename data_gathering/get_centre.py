from data_gathering.data_api import geocode

def get_centre(query):

    centre_coords = geocode(query)

    return centre_coords
