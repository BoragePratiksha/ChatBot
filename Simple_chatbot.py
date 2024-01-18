import nltk
from nltk.chat.util import Chat, reflections

# Define the chat pairs
pairs = [
    ["my name is (.*)", ["Hello %1! How can I help you today?"]],
    ["(hi|hello|hey)", ["Hi there! How can I assist you?"]],
    ["what is your name?", ["I'm a simple chatbot. You can call me ChatGPT."]],
    ["how are you?", ["I'm just a computer program, but thanks for asking!"]],
    ["(.*) your name?", ["I am a chatbot created with NLTK."]],
    ["quit", ["Goodbye! Have a great day."]],
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Hello! I'm your chatbot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break
    else:
        response = chatbot.respond(user_input)
        print("Chatbot:", response)


