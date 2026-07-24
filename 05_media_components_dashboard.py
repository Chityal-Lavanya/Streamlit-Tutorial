import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Media Components",
    layout="wide"
)

st.title("Media Components Dashboard")

# Image
st.header("Image Upload")
image = st.file_uploader(
    "Upload an Image",
    type= ["png","jpg","jpeg"],
    key="image"
)
if image:
    st.image(image, caption="Uploaded Image", use_container_width=True)

# Audio
st.header("Audio Upload")
audio = st.file_uploader(
    "Upload an Audio File",
    type= ["mp3", "wav", "ogg"],
    key="audio"
)
if audio:
    st.audio(audio)

# Video
st.header("Video Upload")
video = st.file_uploader(
    "Upload a Video",
    type= ["mp4","mov","avi"],
    key="video"
)
if video:
    st.video(video)

# Camera Input
st.header("Camera")
photo = st.camera_input("Capture Photo")
if photo:
    st.success("Photo Captured Successfully!")
    st.image(photo)

# File Upload
st.header("Upload Any File")
uploaded_file = st.file_uploader(
    "Upload Document",
    type= ["pdf","txt","csv","xlsx"]
)
if uploaded_file:
    st.write("Filename:", uploaded_file.name)
    st.write("File Size:",uploaded_file.size,"bytes")
    st.success("File Uploaded Successfully!")

# Download Button
st.header("Download Sample Report")
report = """
Media Components

Image Display
Audio Player
Video Player
Camera Input
File Upload
Download Button
"""
st.download_button(
    label="Download Report",
    data=report,
    file_name="media_report.txt",
    mime="text/plain"
)
st.success("Media Components Demonstration Completed")

