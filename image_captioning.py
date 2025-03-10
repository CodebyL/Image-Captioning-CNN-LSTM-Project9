import tensorflow as tf
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, Embedding, Dense
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load a pre-trained CNN model (InceptionV3) to extract image features
base_model = InceptionV3(weights='imagenet')
cnn_model = Model(base_model.input, base_model.layers[-2].output)  # Remove last layer

def preprocess_image(image_path):
    """Prepares the image for CNN processing."""
    img = Image.open(image_path).resize((299, 299))  # Resize image
    img = np.array(img) / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

def extract_features(image_path):
    """Extracts features from an image using InceptionV3."""
    img = preprocess_image(image_path)
    return cnn_model.predict(img)  # Get feature vector

# Simple vocabulary and example captions
word_to_index = {"<start>": 1, "<end>": 2, "dog": 3, "playing": 4, "grass": 5}
index_to_word = {v: k for k, v in word_to_index.items()}
vocab_size = len(word_to_index) + 1  # +1 for padding

# Build a very simple LSTM-based captioning model
embedding_dim = 128
max_length = 5  # Short caption length

inputs = Input(shape=(2048,))  # Image feature input
hidden = Dense(embedding_dim, activation='relu')(inputs)  # Process image features
lstm_input = Input(shape=(max_length,))  # Caption input
embedding = Embedding(vocab_size, embedding_dim, mask_zero=True)(lstm_input)
lstm = LSTM(256, return_sequences=True)(embedding)  # LSTM for text
output = Dense(vocab_size, activation='softmax')(lstm)  # Predict next word
caption_model = Model([inputs, lstm_input], output)

# Function to generate a simple caption (mock output)
def generate_caption(image_features):
    """Returns a simple hardcoded caption for testing."""
    return "A dog playing in grass."

# Load an example image
image_path = "example.jpg"  # Replace with actual image path
features = extract_features(image_path)  # Extract image features
caption = generate_caption(features)  # Generate caption

# Display image with generated caption
img = Image.open(image_path)
plt.imshow(img)
plt.axis("off")
plt.title("Generated Caption: " + caption)
plt.show()