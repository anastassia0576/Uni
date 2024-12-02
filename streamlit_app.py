import streamlit as st
import folium
from folium.plugins import Search, MarkerCluster
from io import BytesIO

# GeoJSON данные
geojson_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {"name": "Корпус агрономического факультета КазАТУ", "category": "Category B"},
            "geometry": {"coordinates": [71.41037773710028, 51.186010264645375], "type": "Point"},
        },
        {
            "type": "Feature",
            "properties": {"name": "Казахский агротехнический университет имени С. Сейфуллина, главный корпус"},
            "geometry": {"coordinates": [71.40919952047997, 51.18714511950674], "type": "Point"},
        },
        # Добавьте остальные объекты из вашего GeoJSON...
    ],
}

# Создаем карту Folium
m = folium.Map(location=[51.186845, 71.41058], zoom_start=14)

# Кластеризация маркеров
marker_cluster = MarkerCluster()

for feature in geojson_data["features"]:
    coords = feature["geometry"]["coordinates"]
    name = feature["properties"]["name"]

    popup_content = f"<b>Name:</b> {name}<br><b>Category:</b>"

    marker = folium.Marker(
        location=[coords[1], coords[0]],
        popup=popup_content,
        tooltip=name,
        icon=folium.Icon(color="blue", icon="info-sign"),
    )
    marker_cluster.add_child(marker)

# Добавляем кластер маркеров на карту
m.add_child(marker_cluster)

# Добавляем слой GeoJSON с поиском
geojson_layer = folium.GeoJson(
    geojson_data,
    name="GeoJSON Data",
    popup=folium.GeoJsonPopup(fields=["name"]),
    tooltip=folium.GeoJsonTooltip(fields=["name"], aliases=["Name:"]),
)
m.add_child(geojson_layer)

# Добавляем компонент поиска
search = Search(
    layer=geojson_layer,
    geom_type="Point",
    placeholder="Найти объект на карте",
    search_label="name",
    collapsed=False,
).add_to(m)

# Добавляем управление слоями
folium.LayerControl().add_to(m)

# Сохранение карты в объект BytesIO
map_html = BytesIO()
m.save(map_html, close_file=False)

# Отображение карты в Streamlit
st.components.v1.html(map_html.getvalue().decode(), height=600)
