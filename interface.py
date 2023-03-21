from data_gathering.data_api import geocode, bikepoint_api
from data_cleaning.clean_data import create_dataframe, clean_dataframe, add_df_columns
from visualizing.nearby_bikes import bikepoints_near_me

from params import API_KEY

def main_pipeline():

    # Get the data from the API
    res = bikepoint_api(app_key=API_KEY)

    # Create dataframe
    df = create_dataframe(api_output=res)

    # Basic df cleaning
    df_clean = add_df_columns(clean_dataframe(df))

    return df_clean

