import plotly.express as px
import plotly.graph_objects as go

from data_gathering.get_centre import get_centre

from ml_logic.params import MAPBOX_TOKEN

def bikepoints_near_me(query, dataframe):

    token = MAPBOX_TOKEN

    query += ', London'

    centre_coords = get_centre(query)

    fig = go.Figure()

    fig.add_trace(go.Scattermapbox(mode = "markers"
                                   , lon = [centre_coords['lon']], lat = [centre_coords['lat']]
                                   , marker = {'size': 20, 'symbol': ["marker"]}
                                   , text = ["You are here!"]
                                   , name='You are here!'
                                   , showlegend=False)
                  )

    fig.add_traces(
        list(px.scatter_mapbox(dataframe,
                            lat='lat'
                            , lon='lon'
                            , color='bike_availability'
                            , size='number_bikes'
                            , zoom=15
                            , center=centre_coords
                            , color_continuous_scale=['red', 'grey', 'green']
                            , mapbox_style='carto-positron'
                            , width=800
                            , height=600
                            , labels={'number_bikes': 'Number of bikes',
                                'bike_availability': '% of total',
                                'Name': 'Bikepoint name'}
                            , hover_name='Name'
                            , hover_data={'Name': False,
                                'number_bikes': True,
                                'bike_availability': True,
                                'lat': False,
                                'lon': False}).select_traces()
             )
        )

    fig.update_layout(width=800
                      , height=600
                      , mapbox=dict(accesstoken=token
                                    , center=go.layout.mapbox.Center(lat=centre_coords['lat']
                                                                     , lon=centre_coords['lon'])
                                    , zoom=15)
                      )

    return fig
