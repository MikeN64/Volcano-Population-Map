import folium
import pandas

data = pandas.read_csv("Volcanoes.csv")
lats = list(data["LAT"])
lons = list(data["LON"])
names = list(data["NAME"])
elevs = list(data["ELEV"])

START_POINT = (38.58, -99.09)

map = folium.Map(location=START_POINT, zoom_start=6, tiles="Stamen Terrain")

feature_group = folium.FeatureGroup(name="Volcanos Map")

for lat, lon, name, elev in zip(lats, lons, names, elevs):
    popup_str = name + "\n" + str(elev) + "m"
    feature_group.add_child(folium.Marker(location=(lat, lon), popup=popup_str, icon=folium.Icon(color="green")))

map.add_child(feature_group)

map.save("map1.html")