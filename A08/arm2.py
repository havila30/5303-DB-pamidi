import numpy as np 
import pandas as pd
import plotly
import plotly.graph_objects as go
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["armageddon"]
token = "pk.eyJ1IjoiaHBhbWlkaS0wNzMwIiwiYSI6ImNrMjl6NW8yODE4ZGEzY29qdnJ3Y3BxNHAifQ.iauTC3HeE6Pslwajw4738A"
volcanos = db["volcanos"]
mapbox_style = "mapbox://styles/hpamidi-0730/ck40pr98p0j4b1cklszn224pj"

volcano_List = []
Latitudes = []
Longitude = []
for obj in volcanos.find():
    volcano_List.append(db["volcanos"].find().sort([("PEI", -1)]))
    Latitudes.append(obj["latitude"])
    Longitude.append(obj["longitude"])
Plot = go.Figure()

Plot.add_trace(go.Scattermapbox(
                                    lat = Latitudes,
                                    lon = Longitude,
                                    mode = "markers",   
                                    marker = {"size":[25, 15, 10],
                                    "color":["Red", "Orange", "Yellow"]},
                                    name="Top 3 worst PEI's"
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
            zoom=3
        ))

Plot.show()
plotly.offline.plot(Plot, filename='arm2.html')