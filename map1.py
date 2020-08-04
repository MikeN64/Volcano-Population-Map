import folium

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
map.save("map1.html")