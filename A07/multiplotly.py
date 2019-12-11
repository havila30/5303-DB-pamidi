import plotly
import plotly.graph_objects as go
from geo import mapbox_access_token
from geo import run_country_border
from geo import run_bbox
from geo import run_airports
from geo import run_earthquakes
from geo import run_ufos

if __name__ == '__main__':
    mapbox_style = "mapbox://styles/hpamidi-0730/ck40pr98p0j4b1cklszn224pj"

    airports_latitude,airports_longitude = run_airports()
    earthquake_Latitude, earthquake_Longitude = run_earthquakes()
    ufos_Latitude, ufos_Longitude = run_ufos()
    
    airports = [go.Scattermapbox(
        lat=airports_latitude,
        lon = airports_longitude,
        mode = 'markers',
        marker=dict(
            size=4,
            color='blue',
            opacity = .5,
        ),
        name='Airports'
    )]

    ufos = [go.Scattermapbox(
        lat=ufos_Latitude,
        lon = ufos_Longitude,
        mode = 'markers',
        marker=dict(
            size=4,
            color='green',
            opacity = .5,
        ),
        name='Ufo Sightings'
    )]


    earthquakes = [go.Scattermapbox(
        lat=earthquake_Latitude,
        lon = earthquake_Longitude,
        mode = 'markers',
        marker=dict(
            size=4,
            color='orange',
            opacity = .5,
        ),
        name='Earthquakes'
    )]

    layout = go.Layout(autosize=True,
    mapbox = dict(accesstoken= mapbox_access_token,
    bearing=0,
    pitch=0,
    zoom=5,
    center=dict(lat=0,lon=0),
    style=mapbox_style),
    width=1500,
    height=1080,
    title = "Armageddon")

    plotting_of_earthquake = dict(data=earthquakes, layout=layout)
    plotly.offline.plot(plotting_of_earthquake, filename='earthquakes.html')
    plotting_of_ufos= dict(data=ufos, layout=layout)
    plotly.offline.plot(plotting_of_ufos, filename='ufos.html')
    plotting_of_airports = dict(data=airports, layout=layout)
    plotly.offline.plot(plotting_of_airports, filename='airports.html')