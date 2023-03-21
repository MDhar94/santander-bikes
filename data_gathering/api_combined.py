from data_gathering.api_individual import get_bikepoint_info, get_bikepoint_id

def bikepoint_info_request(search_query, app_key):

    """Combine both bikepoint functions into one!"""

    id_list = get_bikepoint_id(search_query, app_key)

    bikepoint_info = get_bikepoint_info(id_list, app_key)

    return bikepoint_info
