import requests

#######################################################
######## CALL THE API TO GET THE RELEVANT DATA ########
#######################################################

def get_bikepoint_id(search_query, app_key):

    """Return a list of IDs of bikepoints that are located within
    the search query that is specified"""

    base_url = 'https://api.tfl.gov.uk/BikePoint/Search'
    params_dict = {'app_key':app_key
                       ,'query':f'{search_query}'}

    res = requests.get(base_url,params_dict).json()

    id_list = [value['id'] for value in res]

    return id_list


def get_bikepoint_info(id_list, app_key):

    """Based on a list of bikepoint IDs, return the relevant metrics
    for said bikepoints"""

    base_url = 'https://api.tfl.gov.uk/BikePoint'
    params_dict = {'app_key':app_key}

    res = requests.get(base_url,params_dict).json()

    bikepoints = [bikepoint for bikepoint in res if bikepoint['id'] in id_list]

    print(len(id_list))

    return bikepoints
