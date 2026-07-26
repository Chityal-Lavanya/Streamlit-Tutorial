import streamlit as st
import pandas as pd
import pydeck as pdk
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Module 8 Maps Dashboard", layout="wide")

st.title("🗺️ Module 8: Maps & Geographical Data Dashboard")

locations = pd.DataFrame({
    "City": ["Pune", "Mumbai", "Delhi", "Bengaluru"],
    "lat": [18.5204, 19.0760, 28.6139, 12.9716],
    "lon": [73.8567, 72.8777, 77.2090, 77.5946]
})

selected = st.sidebar.selectbox("Select City", locations["City"])

city = locations[locations["City"] == selected].iloc[0]

st.subheader("Selected Location")
st.write(city)

st.subheader("Location Table")
st.dataframe(locations)

st.subheader("1. Streamlit Map")
st.map(locations[["lat", "lon"]])

st.subheader("2. PyDeck Map")

layer = pdk.Layer(
    "ScatterplotLayer",
    data=locations,
    get_position="[lon, lat]",
    get_radius=30000,
    get_fill_color=[0, 128, 255]
)

view = pdk.ViewState(
    latitude=city["lat"],
    longitude=city["lon"],
    zoom=5
)

st.pydeck_chart(
    pdk.Deck(
        layers=[layer],
        initial_view_state=view
    )
)

st.subheader("3. Folium Map")

m = folium.Map(
    location=[city["lat"], city["lon"]],
    zoom_start=6
)

for _, row in locations.iterrows():
    folium.Marker(
        [row["lat"], row["lon"]],
        popup=row["City"]
    ).add_to(m)

st_folium(m, width=900, height=500)