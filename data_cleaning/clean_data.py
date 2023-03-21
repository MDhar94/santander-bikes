import pandas as pd
import numpy as np

# all_bikepoints = all_bikepoint_info(app_key)

def create_dataframe(api_output):

    # Create dict to become dataframe
    all_bikepoint_dict = {
        'Name': [],
        'lat': [],
        'lon': [],
        'number_docks': [],
        'number_bikes': [],
        'number_ebikes': []
    }

    # Assign values to dictionary
    for bikepoint in api_output:

        xtras = 'additionalProperties'

        # Name
        all_bikepoint_dict['Name'].append(bikepoint['commonName'])

        # Coords
        all_bikepoint_dict['lat'].append(bikepoint['lat'])
        all_bikepoint_dict['lon'].append(bikepoint['lon'])

        # Docks
        all_bikepoint_dict['number_docks'].append(bikepoint[xtras][8]['value'])

        # Bikes
        all_bikepoint_dict['number_bikes'].append(bikepoint[xtras][6]['value'])

        # E-Bikes
        all_bikepoint_dict['number_ebikes'].append(bikepoint[xtras][-1]['value'])

    # Convert dictionary to dataframe
    all_bikepoint_df = pd.DataFrame(all_bikepoint_dict)

    return all_bikepoint_df

def clean_dataframe(dataframe):

    for col in dataframe.columns:

        dataframe[col].replace('', np.nan, inplace=True)

    dataframe.dropna(inplace=True)

    dataframe = dataframe.astype({
        'number_docks': 'int32',
        'number_bikes': 'int32',
        'number_ebikes': 'int32'
    })

    dataframe = dataframe.copy()[dataframe['number_docks']>0]

    return dataframe

def add_df_columns(dataframe):

    dataframe['classic_bikes'] = dataframe['number_bikes'] - dataframe['number_ebikes']

    dataframe['bike_availability'] = round(
        (dataframe['number_bikes'] / dataframe['number_docks']
         ) *100, 0)

    dataframe['ebike_availability'] = round(
        (dataframe['number_ebikes'] / dataframe['number_docks']
         ) *100, 0)

    return dataframe
