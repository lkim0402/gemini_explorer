# Gemini Explorer

Gemini Explorer is a Streamlit application that integrates with Google Vertex AI to provide an interactive chatbot experience using the Gemini model. The application allows users to interact with an AI-powered assistant named ReX.

## Features

- Interactive chatbot powered by Google Vertex AI
- Uses the Gemini model for generating responses
- Easy-to-use Streamlit interface

## Prerequisites

- Python 3.7 or higher
- Google Cloud account with Vertex AI enabled
- Service account with appropriate permissions


## Usage

1. Initialize Vertex AI and run the Streamlit application:

    ```bash
    streamlit run gemini_explorer.py
    ```

2. Open the provided local URL in your web browser.

3. Interact with the AI assistant, ReX, by entering your queries in the chat input.

## Code Overview

- `gemini_explorer.py`: Main script to run the Streamlit application. Initializes Vertex AI and handles user interactions.
- `requirements.txt`: List of Python packages required for the project.
