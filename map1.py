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

def produce_marker_color(elev):
    LOW = 1000
    HIGH = 3000

    if elev <= LOW:
        return "green"
    if LOW < elev < HIGH:
        return "orange"
    if elev >= HIGH:
        return "red"
    return "gray"

def style_population(polygon):
    LOW = 10000000
    HIGH = 20000000

    population = polygon["properties"]["POP2005"]
    styles = {}

    if population <= LOW:
        styles = {"fillColor": "green"}
    elif LOW < population < HIGH:
        styles = {"fillColor": "orange"}
    elif population >= HIGH:
        styles = {"fillColor": "red"}

    return styles 

map = folium.Map(location=START_POINT, zoom_start=5, tiles="Stamen Terrain")

feature_group = folium.FeatureGroup(name="Volcanos Map")

for lat, lon, name, elev in zip(lats, lons, names, elevs):
    iframe = folium.IFrame(html=html.format(name, name, elev), width=200, height=100)
    circle_marker = folium.CircleMarker(location=(lat, lon), popup=folium.Popup(iframe), fill_color=produce_marker_color(elev), color="grey", fill_opacity=0.7)
    feature_group.add_child(circle_marker)

geo_json = folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), style_function=style_population)
feature_group.add_child(geo_json)

map.add_child(feature_group)

map.save("map1.html")