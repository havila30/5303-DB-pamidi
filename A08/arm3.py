import numpy as np 
import pandas as pd
import plotly
import plotly.graph_objects as go
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["armageddon"]
token = "pk.eyJ1IjoiaHBhbWlkaS0wNzMwIiwiYSI6ImNrMjl6NW8yODE4ZGEzY29qdnJ3Y3BxNHAifQ.iauTC3HeE6Pslwajw4738A"
mapbox_style = "mapbox://styles/hpamidi-0730/ck40pr98p0j4b1cklszn224pj"
Plane_Crash = db["plane_crashes"]
latitudes = []
longitudes = []
Lat_R_300 = []
Lat_O_200 = []
Lat_Y_100 = []
Left_crash_lat_B = []
Lon_R_300 = []
Lon_O_200 = []
Lon_Y_100 = []
Left_crash_lon_B = []

for object in Plane_Crash.find():
    latitudes.append(object["Latitude"])
    longitudes.append(object["Longitude"])
    if(object["TotalFatalInjuries"]!='  ' and object["TotalFatalInjuries"] is not None):
     if (int(object["TotalFatalInjuries"]) > 300):
        Lat_R_300.append(object["Latitude"])
        Lon_R_300.append(object["Longitude"])
     elif (int(object["TotalFatalInjuries"]) > 200):
        Lat_O_200.append(object["Latitude"])
        Lon_O_200.append(object["Longitude"])
     elif (int(object["TotalFatalInjuries"]) > 100):
        Lat_Y_100.append(object["Latitude"])
        Lon_Y_100.append(object["Longitude"])
     else:
        Left_crash_lat_B.append(object["Latitude"])
        Left_crash_lon_B.append(object["Longitude"])

Plot = go.Figure()

Plot.add_trace(go.Scattermapbox(
                                    lat = Lat_R_300,
                                    lon = Lon_R_300,
                                    mode = "markers",   
                                    marker = {"size": 25, "color": "red"},
                                    name = "worst plane crashes over 300"
                                    )
                                )

Plot.add_trace(go.Scattermapbox(
                                    lat = Lat_O_200,
                                    lon = Lon_O_200,
                                    mode = "markers",   
                                    marker = {"size": 25, "color": "orange"},
                                    name = "worst plane crashes over 200"
                                    )
                                )                                

Plot.add_trace(go.Scattermapbox(
                                    lat = Lat_Y_100,
                                    lon = Lon_Y_100,
                                    mode = "markers",   
                                    marker = {"size": 25, "color": "yellow"},
                                    name = "worst plane crashes over 100"
                                    )
                                )

Plot.add_trace(go.Scattermapbox(
                                    lat = Left_crash_lat_B,
                                    lon = Left_crash_lon_B,
                                    mode = "markers",   
                                    marker = {"size": 25, "color": "blue"},
                                    name = "worst plane crashes left over"
                                    )
                                )      


Plot.update_layout(
        autosize=True,
        hovermode='closest',
        mapbox=go.layout.Mapbox(
            accesstoken=token,
            bearing=0,
            style=mapbox_style,
            center=go.layout.mapbox.Center(
                lat=33.930828,
                lon=-98.484879
            ),
            pitch=0,
            zoom=1
        ))

plotly.offline.plot(Plot, filename='arm3.html')