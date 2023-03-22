from data_gathering.data_api import bikepoint_api
from data_cleaning.calculate_distance import get_coordinate_distance
from data_cleaning.clean_data import create_dataframe, clean_dataframe, add_df_columns

from ml_logic.params import API_KEY

# Predict walking times from coords to bikepoint of choice?
# Predict likelihood of getting a bike given time of day, day, bikepoint, etc.?

def clean_pipeline():

    # Get the data from the API
    res = bikepoint_api(app_key=API_KEY)

    # Create dataframe
    df = create_dataframe(api_output=res)

    # Basic df cleaning
    df_clean = add_df_columns(clean_dataframe(df))

    return df_clean

def ten_nearest_bikes(query):

    query = query
    df = clean_pipeline()

    user_df = df.copy()

    user_df['distance'] = df['coords'].apply(get_coordinate_distance, query=query)
    user_df.sort_values(by='distance',ascending=True, inplace=True)

    closest_top10 = user_df.head(10)[['Name','distance','number_bikes','number_docks']]
    closest_top10.reset_index(inplace=True,drop=True)

    return closest_top10


if __name__ == '__main__':

    df_clean = clean_pipeline()

    print(df_clean.head())
