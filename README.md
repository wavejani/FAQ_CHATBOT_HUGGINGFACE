---
title: FAQ_Chatbot
app_file: app.py
sdk: gradio
sdk_version: 4.39.0
---
# FAQ AI Chatbot

## Overview

This project is a proof of concept/prototype demo of a RAG AI chatbot using Hugging Face's language model and FAISS for custom FAQ data retrieval, and Gradio for the user interface.

## Setup

1. **Clone the repository:**

   ```sh
   git clone <repository_url>
   cd faq_chatbot_hf
   ```

2. **Create and activate a vistual environment**

   ```
   python -m venv .venv
   source .venv/bin/activate    # On Windows, use `.venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```
   pip install -r src/requirements.txt
   ```

4. **Run the application:**

   ```
   python app.py
   ```

## Docker Setup

1. **Build the Docker image:**

   ```
   docker build -t faq_chatbot_hf .
   ```

2. **Run the Docker container:**

   ```
   docker-compose up
   ```

## Usage (after running: python app.py)

Go to the local URL (http...) or public URL (https...) informed on the terminal commandline to interact with the chatbot.

## Testing

Ask questions (sentences or words) related to FAQ data:

How can i withdraw profits?
What leverage is available?
Account. Funds. Refund. Trader. Profit. Verified. Payment.

Say something else to test the chatbots capabilities:

Hello. Thank you. Goodbye. How are you. I am...

## About the Hugging Face DistilGPT2 LLM model

This model has it's pros and cons. Small size (good). Free to use (good). Everything else (pretty bad). But can be used for this kind of FAISS data usage testing in AI chatbot settings and prototyping. Not at all ideal as a general chatbot LLM. Hard to fine-tune to be a effective universal chatbot. Generates mostly jibberish. Can finalize sentenced: I am... Where is...But thats about it.

Anyways, overall great chatbot to finding custom FAISS data.

Overall, this chatbots performance would be much better by using OPENAI's (etc) newest paid LLM models, with their API KEY's.

Out-of-scope Uses:

OpenAI states in the GPT-2 model card:

    "Because large-scale language models like GPT-2 do not distinguish fact from fiction, we don’t support use-cases that require the generated text to be true.

    Additionally, language models like GPT-2 reflect the biases inherent to the systems they were trained on, so we do not recommend that they be deployed into systems that interact with humans unless the deployers first carry out a study of biases relevant to the intended use-case."

DistilGPT2 (short for Distilled-GPT2) is an English-language model pre-trained with the supervision of the smallest version of Generative Pre-trained Transformer 2 (GPT-2). Like GPT-2, DistilGPT2 can be used to generate text. Users of this model card should also consider information about the design, training, and limitations of GP-2.

The developers of GPT-2 state in their model card that they envisioned GPT-2 would be used by researchers to better understand large-scale generative language models, with possible secondary use cases including:

Writing assistance: Grammar assistance, autocompletion (for normal prose or code)
Creative writing and art: exploring the generation of creative, fictional texts; aiding creation of poetry and other literary art.
Entertainment: Creation of games, chat bots, and amusing generations.

More info: https://huggingface.co/distilbert/distilgpt2
