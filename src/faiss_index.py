import faiss
import numpy as np
import os
import re
import logging
from sentence_transformers import SentenceTransformer

# Configure logging
logging.basicConfig(level=logging.INFO)

# FaissIndex class to handle indexing and searching of FAQs using FAISS
class FaissIndex:
    def __init__(self, vector_size):
        self.index = faiss.IndexFlatL2(vector_size)  # Initialize FAISS index
        self.faqs = []  # List to store FAQs
        self.vector_size = vector_size  # Dimension of the vectors
        self.model = SentenceTransformer('all-MiniLM-L6-v2')  # Use a pre-trained model for vectorization

    def clean_text(self, text):
        # Function to clean the text, removing hyperlinks and special characters
        text = re.sub(r'\[HYPERLINK:.*?\]', '', text)  # Remove hyperlinks
        text = re.sub(r'\s+', ' ', text)  # Remove excessive whitespace
        return text.strip()  # Strip leading and trailing whitespace

    def add_faqs(self, faq_dir):
        # Function to add FAQs from text files in the specified directory
        for file_name in os.listdir(faq_dir):
            if file_name.endswith('.txt'):  # Process only text files
                file_path = os.path.join(faq_dir, file_name)
                logging.info(f"Processing file: {file_path}")
                try:
                    with open(file_path, 'r') as file:
                        faq = file.read().strip()  # Read and strip the FAQ content
                        faq = self.clean_text(faq)  # Clean the FAQ content
                        if faq:
                            vector = self.vectorize(faq)  # Vectorize the FAQ
                            self.index.add(np.array([vector]))  # Add vector to FAISS index
                            self.faqs.append(faq)  # Add FAQ to the list
                        else:
                            logging.warning(f"Warning: FAQ in file {file_path} is empty.")
                except Exception as e:
                    logging.error(f"Error processing file {file_path}: {e}")

    def search(self, query, k=1):
        # Function to search the FAISS index for the closest FAQs to the query
        try:
            vector = self.vectorize(query)  # Vectorize the query
            distances, indices = self.index.search(np.array([vector]), k)  # Search the index
            results = [(self.faqs[i], distances[0][j]) for j, i in enumerate(indices[0])]  # Get search results
            logging.info(f"Search results: {results}")
            return results
        except Exception as e:
            logging.error(f"Error searching the FAISS index: {e}")
            return [("Error: Could not process your query at this time.", 1.0)]

    def vectorize(self, text):
        return self.model.encode(text)  # Use the pre-trained model to convert text to vectors
