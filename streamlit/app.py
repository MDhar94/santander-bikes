import streamlit as st
import plotly.express as px

from interface import main_pipeline
from visualizing.nearby_bikes import bikepoints_near_me

#################
# 'try, except' to prevent error dialogue?
# button to get user coords based on gps?
#################

# Title for the homepage
st.header('Santander bikes near me')

# Load the data function
@st.cache
def get_clean_data():

    df = main_pipeline()

    return df

df = get_clean_data()

# Load the nearby chart

bike_loc = st.text_input(label="Please enter the area you want to see:")

fig = bikepoints_near_me(query=bike_loc
                         , dataframe=df)

if bike_loc != "":
    st.plotly_chart(fig)