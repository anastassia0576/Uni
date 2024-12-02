import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import requests

import folium
from folium.plugins import Search, MarkerCluster

geojson_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
      "properties": {"name": "Корпус агрономического факультета КазАТУ", "category": "Category B"},
      "geometry": {
        "coordinates": [
          71.41037773710028,
          51.186010264645375], "type": "Point"},
        },
        {
            "type": "Feature",
      "properties": {"name": "Казахский агротехнический университет имени С. Сейфуллина, главный корпус"},
      "geometry": {
        "coordinates": [
          71.40919952047997,
          51.18714511950674], "type": "Point"},
        },
        {
            "type": "Feature",
      "properties": {"name": "Биологический корпус КазАТУ"},
      "geometry": {
        "coordinates": [
          71.4094857538959,
          51.18797538164955], "type": "Point"},
        },
        {
            "type": "Feature",
      "properties": {"name": "Корпус технического факультета КазАТУ"},
      "geometry": {
        "coordinates": [
          71.41114324507092,
          51.1877459137084], "type": "Point"},
        },
        {
            "type": "Feature",
      "properties": {"name": "Новый корпус технического факультета КазАТУ"},
      "geometry": {
        "coordinates": [
          71.41172902508583,
          51.18715346392423], "type": "Point"},
        },
        {
            "type": "Feature",
      "properties": {"name": "Корпус военной кафедры КазАТУ "},
      "geometry": {
        "coordinates": [
          71.41081041551712,
          51.18707001968042], "type": "Point"},
        },
        {
            "type": "Feature",
      "properties": {"name": "Склад КазАТУ "},
      "geometry": {
        "coordinates": [
          71.41170239872159,
          51.18659438460773], "type": "Point"},
        },
        {
            "type": "Feature",
      "properties": {"name": "Общежитие №7 КазАТУ "},
      "geometry": {
        "coordinates": [
          71.41260769510728,
          51.1863148424068], "type": "Point"},
        },
        {
            "type": "Feature",
      "properties": {"name": "Общежитие №2б КазАТУ "},
      "geometry": {
        "coordinates": [
         71.41294052466108,
          51.18694068080447], "type": "Point"},
        },
        {
            "type": "Feature",
      "properties": {"name": "Общежитие №9 КазАТУ "},
      "geometry": {
        "coordinates": [
         71.4132400712582,
          51.18633153154096], "type": "Point"},
        },
        {
            "type": "Feature",
      "properties": {"name": "Общежитие №4 КазАТУ "},
      "geometry": {
        "coordinates": [
         71.41429301517488,
          51.18643214747047], "type": "Point"},
        },
        {
            "type": "Feature",
      "properties": {"name": "Корпус земельного факультета КазАту "},
      "geometry": {
        "coordinates": [
         71.41529891243619,
          51.18658181999851], "type": "Point"},
        },
        {
            "type": "Feature",
      "properties": {"name": "Общежитие №5 КазАТУ "},
      "geometry": {
        "coordinates": [
         71.41385674718038,
          51.18641280852361], "type": "Point"},
        },
        {
            "type": "Feature",
      "properties": {"name": "Гараж КазАТУ "},
      "geometry": {
        "coordinates": [
         71.41107883675795,
          51.186700066345196], "type": "Point"},
        },
        {
            "type": "Feature",
      "properties": {"name": "Корпус кафедры технической механики КазАТУ "},
      "geometry": {
        "coordinates": [
         71.41207484233962,
          51.186695146518645], "type": "Point"},
        },
    ],

}

m = folium.Map(location=[51.186845, 71.41058], zoom_start=14)

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

m.add_child(marker_cluster)

geojson_layer = folium.GeoJson(
    geojson_data,
    name="GeoJSON Data",
    popup=folium.GeoJsonPopup(fields=["name"]),
    tooltip=folium.GeoJsonTooltip(fields=["name"], aliases=["Name:"]),
)
m.add_child(geojson_layer)

search = Search(
    layer=geojson_layer,
    geom_type="Point",
    placeholder="Найти объект на карте",
    search_label="name",
    collapsed=False,
).add_to(m)



folium.LayerControl().add_to(m)

m.save("interactive_map.html")

m
