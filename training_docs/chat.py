import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the trained model and tokenizer
model_path = './trained_chatbot'
model = GPT2LMHeadModel.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
tokenizer.pad_token = tokenizer.eos_token

# Function to generate response from the chatbot
def generate_response(question):
    inputs = tokenizer.encode(question + tokenizer.eos_token, return_tensors='pt')
    outputs = model.generate(
        inputs,
        max_length=150,
        num_beams=5,
        no_repeat_ngram_size=2,
        early_stopping=True
    )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def main():
    print("Chat with Innova Tech chatbot (type 'exit' to stop):")
    while True:
        question = input("You: ")
        if question.lower() == 'exit':
            break
        response = generate_response(question)
        print("Bot:", response)

if __name__ == "__main__":
    main()