# Script to demonstrate basic usage of the Ollama API
import ollama

# Initialize Ollama client
client = ollama.Client()

# Set the LLM model to use
model = "llama3.2"
# Define the prompt to send to the model
prompt = "Where are we heading with AI?"

# Generate a response using the specified model and prompt
response = client.generate(model, prompt)
# Print the text response from the model
print(f"Response: {response.response}")