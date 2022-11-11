import json
from plotly.graph_objects import Layout
from plotly import offline

filename = "all_month.json"

# Load the file in python readable json format
with open(filename, encoding="utf-8") as f:
    earthquake_data = json.load(f)

# Get title of the plot from the metadata section of file
title = earthquake_data["metadata"]["title"]

data_file = earthquake_data["features"]

# Get magnitude, longitude, latitude and place info from the file data
mags, lons, lats, infos = [], [], [], []

for i in data_file:
    mags.append(i["properties"]["mag"])
    lons.append(i["geometry"]["coordinates"][0])
    lats.append(i["geometry"]["coordinates"][1])
    infos.append(i["properties"]["title"])

# Design and plot the data
data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": infos,
        "marker": {
            "size": [4 * abs(mag) for mag in mags],
            "color": mags,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]

my_layout = Layout(title=title)

fig = {"data": data, "layout": my_layout}

offline.plot(fig)
