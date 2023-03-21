from data_gathering.data_api import bikepoint_api
from data_cleaning.clean_data import create_dataframe, clean_dataframe, add_df_columns

from params import API_KEY

# Predict walking times from coords to bikepoint of choice?
# Predict likelihood of getting a bike given time of day, day, bikepoint, etc.?

def main_pipeline():

    # Get the data from the API
    res = bikepoint_api(app_key=API_KEY)

    # Create dataframe
    df = create_dataframe(api_output=res)

    # Basic df cleaning
    df_clean = add_df_columns(clean_dataframe(df))

    return df_clean


if __name__ == '__main__':

    df_clean = main_pipeline()

    print(df_clean.head())
