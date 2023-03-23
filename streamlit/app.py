import streamlit as st

from interface.main import clean_pipeline, ten_nearest_bikes
from visualizing.nearby_bikes import bikepoints_near_me
from data_gathering.get_centre import get_centre

#################
# button to get user coords based on gps?
#################

# Title for the homepage
st.title('Santander bike locator')

# Load the main clean data
@st.cache(ttl=30)
def get_clean_data():

    df = clean_pipeline()

    return df

df = get_clean_data()

# Get user input for area to show
st.header('Where are you?')
bike_loc = st.text_input(label="Please enter your location here:")

# Load the ten nearest bikes
@st.cache(ttl=30)
def nearest_bikes(dataframe, query):

    centre = get_centre(query)
    centre = (centre['lat'],centre['lon'])

    df = ten_nearest_bikes(dataframe=dataframe, centre=centre)

    return df

if bike_loc != "":

    try:
        col1, col2 = st.columns([3,2])

        with col1:
            fig = bikepoints_near_me(query=bike_loc, dataframe=df)
            st.plotly_chart(fig,use_container_width=True)

        with col2:

            nearest_bikes_df = nearest_bikes(dataframe=df,query=bike_loc)

            st.subheader('Your nearest bike stations are')
            st.dataframe(nearest_bikes_df)

    except:
        st.error('No bikepoints found, please be more specific with your location', icon="🚨")
