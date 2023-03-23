import geopy.distance

def get_coordinate_distance(x, centre):

    coords1 = x
    coords2 = centre

    distance = geopy.distance.geodesic(coords1, coords2).m

    return distance
