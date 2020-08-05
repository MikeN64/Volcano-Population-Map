import folium
import pandas

data = pandas.read_csv("Volcanoes.csv")
lats = list(data["LAT"])
lons = list(data["LON"])
names = list(data["NAME"])
elevs = list(data["ELEV"])

START_POINT = (38.58, -99.09)

html = """<h4>Volcano Information</h4>
<a href="https://www.google.com/search?q={}" target="_blank">{}</a><br>
Height: {} m
"""

map = folium.Map(location=START_POINT, zoom_start=5, tiles="Stamen Terrain")

feature_group = folium.FeatureGroup(name="Volcanos Map")

for lat, lon, name, elev in zip(lats, lons, names, elevs):
    iframe = folium.IFrame(html=html.format(name, name, elev), width=200, height=100)
    feature_group.add_child(folium.Marker(location=(lat, lon), popup=folium.Popup(iframe), icon=folium.Icon(color="green")))

map.add_child(feature_group)

map.save("map1.html")