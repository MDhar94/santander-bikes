import plotly.express as px

from data_gathering.data_api import geocode

def bikepoints_near_me(query, dataframe):

    free_styles = [
    'open-street-map', 'white-bg', 'carto-positron', 'carto-darkmatter',
    'stamen-terrain', 'stamen-toner', 'stamen-watercolor']

    query += ', London'

    centre_coords = geocode(query)

    fig = px.scatter_mapbox(dataframe,
                            lat='lat',
                            lon='lon',
                            color='bike_availability',
                            size='number_bikes',
                            zoom=15,
                            center=centre_coords,
                            color_continuous_scale=['red', 'grey', 'green'],
                            mapbox_style=free_styles[2],
                            width=800,
                            height=600,
                            labels={
                                'number_bikes': 'Number of bikes',
                                'bike_availability': 'Bikes available (%)',
                                'Name': 'Bikepoint name'
                            },
                            hover_name='Name',
                            hover_data={
                                'Name': False,
                                'number_bikes': True,
                                'bike_availability': True,
                                'lat': False,
                                'lon': False
                            })

    fig.update_layout(coloraxis_colorbar=dict(title=""))

    return fig
