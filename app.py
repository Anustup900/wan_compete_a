import os
import streamlit as st
from PIL import Image

# Set the main directory
main_dir = "wan_alle"  # change this

st.title("WAN FIGHT")

# Loop through each subfolder
for folder_name in sorted(os.listdir(main_dir)):
    folder_path = os.path.join(main_dir, folder_name)
    if os.path.isdir(folder_path):
        st.subheader(folder_name)  # Folder name

        # Collect all image paths
        image_files = [
            os.path.join(folder_path, f)
            for f in os.listdir(folder_path)
            if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
        ]

        # Display images horizontally
        cols = st.columns(len(image_files))
        for idx, img_path in enumerate(image_files):
            with cols[idx]:
                img = Image.open(img_path)
                st.image(img, use_container_width=True)
