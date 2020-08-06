import folium
import pandas

class Map:

    def __init__(self):
        self.START_POINT = (38.58, -99.09)
        self.HTML = """<h4>Volcano Information</h4>
<a href="https://www.google.com/search?q={}" target="_blank">{}</a><br>
Height: {} m
"""
        self.data = pandas.read_csv("Volcanoes.csv")
        self.lats = list(self.data["LAT"])
        self.lons = list(self.data["LON"])
        self.names = list(self.data["NAME"])
        self.elevs = list(self.data["ELEV"])
        self.map = folium.Map(location=self.START_POINT, zoom_start=5, tiles="Stamen Terrain")


    def _color_marker(self, elev):
        LOW = 1000
        HIGH = 3000
        
        color = "gray"

        if elev <= LOW:
            color = "green"
        elif LOW < elev < HIGH:
            color = "orange"
        if elev >= HIGH:
            color = "red"

        return color


    def _style_population(self, polygon):
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

    def create_volcano_feature_group(self):
        volcano_fg = folium.FeatureGroup(name="Volcanos")
        for lat, lon, name, elev in zip(self.lats, self.lons, self.names, self.elevs):
            iframe = folium.IFrame(html=self.HTML.format(name, name, elev), width=200, height=100)
            circle_marker = folium.CircleMarker(location=(lat, lon), popup=folium.Popup(iframe), fill_color=self._color_marker(elev), color="grey", fill_opacity=0.7)
            volcano_fg.add_child(circle_marker)

        return volcano_fg

    
    def create_population_feature_group(self):
        FILE_NAME = "world.json"
        population_fg = folium.FeatureGroup(name="Population")

        geo_json = folium.GeoJson(data=open(FILE_NAME, "r", encoding="utf-8-sig").read(), style_function=self._style_population)
        population_fg.add_child(geo_json)

        return population_fg


    def create_layer_control(self):
        layer_control = folium.LayerControl()
        volcano_fg = self.create_volcano_feature_group()
        population_fg = self.create_population_feature_group()
        
        self.map.add_child(volcano_fg)
        self.map.add_child(population_fg)
        self.map.add_child(layer_control)
    

    def save_map(self):
        FILE_NAME = "map.html"
        self.map.save(FILE_NAME)


if __name__ == "__main__":
    world_map = Map()
    world_map.create_layer_control()
    world_map.save_map()