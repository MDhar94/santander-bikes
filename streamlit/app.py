import streamlit as st
from streamlit_metrics import metric, metric_row

from interface.main import clean_pipeline, ten_nearest_bikes
from visualizing.nearby_bikes import bikepoints_near_me
from data_gathering.get_centre import get_centre

#################
# button to get user coords based on gps?
#################

st.set_page_config(
    page_title="Santander bike locator",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Title for the homepage
st.title('Santander bike locator 🚲')

# Load the main clean data
@st.cache(ttl=30)
def get_clean_data():

    df = clean_pipeline()

    return df

df = get_clean_data()

# Get user input for area to show
st.header('Where are you?')
bike_loc = st.text_input(label="Please enter your location")

# Load the ten nearest bikes
@st.cache(ttl=30)
def nearest_bikes(dataframe, query):

    centre = get_centre(query)
    centre = (centre['lat'],centre['lon'])

    df = ten_nearest_bikes(dataframe=dataframe, centre=centre)

    return df

if bike_loc != "":

    try:

        fig = bikepoints_near_me(query=bike_loc, dataframe=df)
        st.plotly_chart(fig,use_container_width=True)

        nearest_df = nearest_bikes(dataframe=df,query=bike_loc)


        st.subheader('Your closest 5 bikestations are:')

        metric_row({f"{nearest_df['Name'][0]}": " "
                    ,f"{nearest_df['Name'][1]}": " "
                    ,f"{nearest_df['Name'][2]}": " "
                    ,f"{nearest_df['Name'][3]}": " "
                    ,f"{nearest_df['Name'][4]}": " ",})

    except:
        st.error('No bikepoints found, please try again! Hint: use a more specific location input', icon="🚨")
