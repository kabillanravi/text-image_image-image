# Image Search Application

This is an image search application that allows users to search for similar images using either text queries or uploaded images. The backend is built with **FastAPI**, leveraging **CLIP** (Contrastive Language-Image Pre-training) for generating embeddings, and **Pinecone** for vector similarity search. The frontend is powered by **Streamlit**, providing an intuitive interface for users to interact with the system.

The application searches an indexed dataset of Unsplash images stored in Pinecone, returning the top similar images based on the input.

## Features

- **Text-to-Image Search**: Enter a text description (e.g., "Flower") to find visually similar images.
- **Image-to-Image Search**: Upload an image to search for visually similar images in the dataset.
- Uses CLIP embeddings for robust image and text understanding.
- Fast similarity search powered by Pinecone's vector database.
- Responsive frontend with Streamlit for easy user interaction.

## Tech Stack

- **Backend**: FastAPI, Python
- **Embedding Model**: CLIP (openai/clip-vit-base-patch32)
- **Vector Database**: Pinecone
- **Frontend**: Streamlit
- **Dependencies**: See `requirements.txt` for full list

## Prerequisites

Before running the application, ensure you have the following:
- Python 3.8+
- A Pinecone account and API key (set up an index named `image-index-50000` with a dimension of 512)
- An Unsplash dataset indexed in Pinecone (namespace: `image-search-dataset`)
- Required libraries installed (listed in `requirements.txt`)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>