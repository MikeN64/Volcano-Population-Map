import folium

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

feature_group = folium.FeatureGroup(name="My Map")

for coordinates in [[38.2, -99.1], [39.2, -97.1]]:
    feature_group.add_child(folium.Marker(location=coordinates, popup="Hi! I am a marker", icon=folium.Icon(color="green")))

map.add_child(feature_group)

map.save("map1.html")