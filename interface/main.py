import geopy.distance

from data_gathering.data_api import bikepoint_api
from data_cleaning.clean_data import create_dataframe, clean_dataframe, add_df_columns

from ml_logic.params import API_KEY

def clean_pipeline():

    # Get the data from the API
    res = bikepoint_api(app_key=API_KEY)

    # Create dataframe
    df = create_dataframe(api_output=res)

    # Basic df cleaning
    df_clean = add_df_columns(clean_dataframe(df))

    return df_clean

def ten_nearest_bikes(dataframe,centre):

    closest_docks_df = dataframe.copy()

    closest_docks_df['distance'] = closest_docks_df.apply(lambda row: int(round(geopy.distance.geodesic(row['coords']
                                                                                            ,centre).m
                                                                            ,1))
                                                        , axis=1)

    closest_docks_df.sort_values(by='distance',ascending=True, inplace=True)

    closest_top5 = closest_docks_df.head(5)[['Name','distance','number_bikes','number_docks']]
    closest_top5.reset_index(inplace=True,drop=True)

    return closest_top5

if __name__ == '__main__':

    df_clean = clean_pipeline()

    df_ten_nearest_bikes = ten_nearest_bikes(df_clean)
