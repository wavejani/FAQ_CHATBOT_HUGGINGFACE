from transformers import AutoModelForCausalLM, AutoTokenizer

# ChatbotModel class to handle the language model operations
class ChatbotModel:
    def __init__(self, model_name='distilgpt2'):
        
        """
        Initialize the ChatbotModel with the specified model name.
        Load the tokenizer and model from Hugging Face.
        """
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        # Ensure pad_token_id is set to eos_token_id if not already set
        if self.tokenizer.pad_token_id is None:
            self.tokenizer.pad_token_id = self.tokenizer.eos_token_id

    def generate_response(self, input_text):
        
        """
        Generate a response based on the input text.
        Use predefined responses for common prompts and the model for other queries.
        """
        
        # Predefined responses for specific conversational prompts
        common_responses = {
            "hello": "Hello! I'm a AI chatbot here to assist you with FAQ's. How can I help you today?",
            "how are you": "Fantastic! i'm a AI chatbot, ready to help you with your questions!",
            "hi": "Hi there! How can I assist you?",
            "what's your name": "I'm an AI chatbot created to help you with your questions.",
            "thank you": "You're welcome! If you have any other questions, feel free to ask.",
            "bye": "Goodbye! Have a great day!",
        }
        
        # Convert the input to lowercase for case-insensitive matching
        input_lower = input_text.lower()
        for prompt in common_responses:
            if prompt in input_lower:
                return common_responses[prompt]
        
        # Improved context prefix to better guide the model
        context_prefix = "Q: {}\nA:".format(input_text)
        
        # Encode the input text to tensor format
        inputs = self.tokenizer.encode(context_prefix, return_tensors='pt')
        
        # Generate attention mask
        attention_mask = inputs.ne(self.tokenizer.pad_token_id)
        
        # Generate a response using the model
        outputs = self.model.generate(
            inputs,
            attention_mask=attention_mask,
            max_length=150,  # Increased max_length to allow for more detailed responses
            num_return_sequences=1,  # Generate only one response sequence
            no_repeat_ngram_size=2,  # Prevents repeating sequences
            repetition_penalty=1.5,  # Penalize repetition in the output
            temperature=0.7,  # Adjust temperature for creativity vs. determinism
            top_p=0.9,  # Use nucleus sampling
            top_k=50,  # Limit the number of highest probability tokens
            pad_token_id=self.tokenizer.pad_token_id,
            do_sample=True  # Ensure sampling is enabled for temperature and top_p
        )
        
        # Decode the generated tokens to a string
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Post-processing to remove trailing quotes and repetitive content
        if response.startswith(context_prefix):
            response = response[len(context_prefix):]
        
        response = response.strip()
        if response.endswith('"'):
            response = response[:-1].strip()
        
        response_lines = response.split('\n')
        if len(response_lines) > 1 and response_lines[0] in response_lines[1]:
            response = response_lines[1].strip()
        
        return response
