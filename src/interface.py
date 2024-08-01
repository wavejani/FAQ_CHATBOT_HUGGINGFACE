import gradio as gr
import logging
from src.model import ChatbotModel
from src.faiss_index import FaissIndex

# Configure logging to display INFO level messages
logging.basicConfig(level=logging.INFO)

# ChatInterface class to handle the Gradio UI and integrate the chatbot model and FAISS index
class ChatInterface:
    def __init__(self):
        logging.info("Initializing ChatbotModel...")
        self.chatbot_model = ChatbotModel()  # Initialize the chatbot model
        logging.info("ChatbotModel initialized.")
        
        logging.info("Initializing FaissIndex...")
        self.faiss_index = FaissIndex(vector_size=384)  # Initialize FaissIndex with vector size 384
        self.faiss_index.add_faqs('data')  # Add FAQs from the 'data' directory to the FaissIndex
        logging.info("FaissIndex initialized and FAQs added.")

    def respond(self, input_text):
        logging.info(f"Received input: {input_text}")
        faiss_response = self.faiss_index.search(input_text, k=1)  # Search for relevant FAQ response
        logging.info(f"FAISS response: {faiss_response}")
        
        threshold = 1.5  # Set a higher threshold to ensure FAISS responses are used when they are relevant
        if faiss_response and faiss_response[0][1] < threshold:
            response = faiss_response[0][0]  # Use FAISS response if it is relevant
            logging.info(f"Using FAISS response: {response}")
        else:
            logging.info("FAISS response not relevant, using model response.")
            response = self.chatbot_model.generate_response(input_text)  # Use model response if FAISS response is not relevant
            logging.info(f"Using model response: {response}")
        
        return response

def launch_interface():
    chat_interface = ChatInterface()  # Initialize the ChatInterface
    gr.Interface(
        fn=chat_interface.respond,  # Function to generate responses
        inputs="text",  # Input type is text
        outputs="text",  # Output type is text
        title="FAQ CHATBOT",  # Title of the Gradio interface
        description="I'm an AI chatbot using Hugging Face LLM model with Gradio UI"  # Description of the Gradio interface
    ).launch(share=True)  # Launch the interface and generate a shareable link

# Entry point for the application
if __name__ == "__main__":
    launch_interface()  # Launch the Gradio interface
