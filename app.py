import os
import logging

# Disable tokenizers parallelism warning to prevent excessive logging
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Set logging level to INFO to suppress debug logs and show only essential information
logging.basicConfig(level=logging.INFO)

from src.interface import launch_interface

# Entry point for the application
if __name__ == "__main__":
    try:
        print("Starting the application...")  # Inform the user that the application is starting
        launch_interface()  # Call the function to launch the Gradio interface
        print("Application has started.")  # Inform the user that the application has started successfully
    except Exception as e:
        print(f"Error starting the application: {e}")  # Print any exceptions that occur during startup

