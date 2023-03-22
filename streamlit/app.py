import streamlit as st

from interface.main import clean_pipeline, ten_nearest_bikes
from visualizing.nearby_bikes import bikepoints_near_me

#################
# button to get user coords based on gps?
#################

# Title for the homepage
st.header('Santander bikes near me')

# Load the main clean data
@st.cache(ttl=30)
def get_clean_data():

    df = clean_pipeline()

    return df

df = get_clean_data()

# Get user input for area to show
bike_loc = st.text_input(label="Please enter the area you want to see:")

# Load the ten nearest bikes
@st.cache(ttl=30)
def nearest_bikes():

    df = ten_nearest_bikes(query=bike_loc)

    return df

nearest_bikes_df = nearest_bikes()

# Load the map (allow for errors, only show once user input given)
try:
    fig = bikepoints_near_me(query=bike_loc, dataframe=df)
except:
    st.write('No bikepoints found, please be more specific with your location')

if bike_loc != "":
    st.plotly_chart(fig)

    st.dataframe(nearest_bikes_df)
