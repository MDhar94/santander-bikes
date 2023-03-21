from data_gathering.api_combined import bikepoint_info_request

from params import API_KEY

if __name__ == '__main__':

    query = input("Enter search query:")

    res = bikepoint_info_request(search_query=query
                                 , app_key=API_KEY)

    print(res)
