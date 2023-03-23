import plotly.express as px
import plotly.graph_objects as go

from data_gathering.get_centre import get_centre

from ml_logic.params import MAPBOX_TOKEN

def bikepoints_near_me(query, dataframe):

    token = MAPBOX_TOKEN

    query += ', London'

    centre_coords = get_centre(query)

    fig = go.Figure(go.Scattermapbox(mode = "markers"
                                     , lon = dataframe['lon']
                                     , lat = dataframe['lat']
                                     , marker=go.scattermapbox.Marker(size=dataframe['number_bikes']
                                                                      , color=dataframe['bike_availability']
                                                                      , colorscale=['red','grey','green'])
                                     , showlegend=False
                                     , hovertext=dataframe['Name']
                                     , hoverinfo="text"
                                     )
                    )

    fig.add_trace(go.Scattermapbox(mode = "markers"
                                   ,lon = [centre_coords['lon']], lat = [centre_coords['lat']]
                                   , marker = {'size': 20, 'symbol': ["marker"]}
                                   , text = ["You are here!"]
                                   , textposition = "bottom right"
                                   , name='You are here!',showlegend=False
                                   , hoverinfo="text"))

    fig.update_layout(mapbox=dict(accesstoken=token
                                    , center=go.layout.mapbox.Center(lat=centre_coords['lat']
                                                                     , lon=centre_coords['lon'])
                                    , zoom=14))

    return fig
