import geopy.distance

from data_gathering.get_centre import get_centre

def get_coordinate_distance(x, query):

    coords1 = x
    coords2 = get_centre(query)

    distance = geopy.distance.geodesic(coords1, coords2).m

    return distance
