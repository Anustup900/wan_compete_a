import os
import streamlit as st
from PIL import Image

# Set the main directory
main_dir = "wan_alle"  # change this

st.title("WAN FIGHT")

for folder_name in sorted(os.listdir(main_folder)):
    folder_path = os.path.join(main_folder, folder_name)

    if os.path.isdir(folder_path):
        st.subheader(folder_name)  # Folder name as section title

        images = []
        captions = []

        for file_name in sorted(os.listdir(folder_path)):
            if file_name.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                img_path = os.path.join(folder_path, file_name)
                img = Image.open(img_path)
                images.append(img)
                captions.append(os.path.splitext(file_name)[0])  # File name without extension

        if images:
            st.image(images, caption=captions, width=200)