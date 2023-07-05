import folium
import streamlit as st
from streamlit_folium import folium_static

st.title('Map with OpenStreetMap Background')

# Create a Folium map object centered at a specific location
map_osm = folium.Map(location=[51.53576193258828, 4.450525045394898], zoom_start=12)

# Add OpenStreetMap tiles as the base layer
folium.TileLayer('openstreetmap').add_to(map_osm)

# Add markers or other map layers as needed
folium.Marker(location=[51.53576193258828, 4.450525045394898]).add_to(map_osm)

# Display the map using the folium_static function
folium_static(map_osm)

