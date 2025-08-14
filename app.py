import os
import streamlit as st
from PIL import Image
from PIL import Image, UnidentifiedImageError

# Set the main directory
main_folder = "wan_alle"  # change this


# Allowed image filenames (lowercase)
allowed_files = {"ref.png", "garment.jpg", "multi_ref_upscaled_refined.png"}

st.title("WAN FIGHT")

for folder_name in sorted(os.listdir(main_folder)):
    folder_path = os.path.join(main_folder, folder_name)

    if os.path.isdir(folder_path):
        st.subheader(folder_name)

        # Filter only a.png, b.png, c.png
        image_files = [
            f for f in sorted(os.listdir(folder_path))
            if f.lower() in allowed_files
        ]

        if not image_files:
            st.info("No matching images in this folder.")
            continue

        # Display in horizontal columns
        cols = st.columns(len(image_files))

        for idx, file_name in enumerate(image_files):
            img_path = os.path.join(folder_path, file_name)
            try:
                img = Image.open(img_path)
                with cols[idx]:
                    st.image(img, caption=os.path.splitext(file_name)[0], use_container_width=True)
            except UnidentifiedImageError:
                st.warning(f"Skipping invalid image: {file_name}")
