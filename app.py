import os
import streamlit as st
from PIL import Image
from PIL import Image, UnidentifiedImageError

# Set the main directory
main_folder = "wan_alle"  # change this

st.title("WAN FIGHT")

for folder_name in sorted(os.listdir(main_folder)):
    folder_path = os.path.join(main_folder, folder_name)

    if os.path.isdir(folder_path):
        st.subheader(folder_name)  # Folder name as section title

        images = []
        captions = []

        for file_name in sorted(os.listdir(folder_path)):
            if file_name.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif")):
                img_path = os.path.join(folder_path, file_name)
                try:
                    img = Image.open(img_path)
                    images.append(img)
                    captions.append(os.path.splitext(file_name)[0])  # File name without extension
                except UnidentifiedImageError:
                    st.warning(f"Skipping invalid image: {file_name}")

        if images:
            st.image(images, caption=captions, width=200)