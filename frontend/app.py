import streamlit as st
import requests
from PIL import Image
import io

# FastAPI backend URL
BACKEND_URL = "http://localhost:8000"

st.title("🔍 Image Search App")

# Sidebar for search controls
with st.sidebar:
    st.header("Search Options")
    
    # Search type selection
    search_type = st.radio(
        "Select search type:",
        ("Text to Image", "Image to Image")
    )
    
    # Input based on search type
    if search_type == "Text to Image":
        search_query = st.text_input("Enter your search query (e.g. Flower)")
        uploaded_file = None
    else:  # Image to Image
        uploaded_file = st.file_uploader("Upload an image to search", 
                                       type=["jpg", "jpeg", "png"])
        search_query = None
    
    # Search button
    search_button = st.button("Search")

# Main content area for results
if search_button:
    if (search_type == "Text to Image" and search_query) or (search_type == "Image to Image" and uploaded_file):
        with st.spinner("Searching..."):
            try:
                if search_type == "Text to Image":
                    response = requests.get(f"{BACKEND_URL}/search/text/", params={"query": search_query})
                else:  # Image to Image
                    image = Image.open(uploaded_file).convert("RGB")
                    st.image(image, caption="Uploaded Image", use_container_width=True)
                    files = {"file": ("image.jpg", uploaded_file.getvalue(), "image/jpeg")}
                    response = requests.post(f"{BACKEND_URL}/search/image/", files=files)
                
                response.raise_for_status()
                matches = response.json()["matches"]

                # Display results
                st.subheader("Top Similar Images")
                for match in matches:
                    score = match["score"]
                    photo_id = match["id"]
                    url = match["url"]
                    st.write(f"**Photo ID**: {photo_id} | **Similarity Score**: {score:.4f}")
                    try:
                        img_response = requests.get(url, stream=True)
                        img_response.raw.decode_content = True
                        img = Image.open(img_response.raw)
                        st.image(img, caption=f"Photo ID: {photo_id}", use_container_width=True)
                    except Exception as e:
                        st.error(f"Could not load image from {url}: {e}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to backend: {e}")
    else:
        st.warning("Please provide a search query or upload an image!")

# Instructions
st.write("---")
st.write("Note: This app searches an Unsplash dataset indexed in Pinecone using CLIP embeddings based on your input.")