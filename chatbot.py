# -----------------------------------------
# Basic Chatbot
# CodeAlpha Python Internship
# -----------------------------------------

def chatbot_response(user_input):

    user_input = user_input.lower()

    if user_input == "hello":
        return "👋 Hello! Nice to meet you."

    elif user_input == "hi":
        return "😊 Hi there!"

    elif user_input == "how are you":
        return "I'm doing great! Thanks for asking."

    elif user_input == "what is your name":
        return "My name is CodeAlpha Bot."

    elif user_input == "who created you":
        return "I was created using Python."

    elif user_input == "help":
        return "You can say Hello, Hi, How are you, Bye."

    elif user_input == "bye":
        return "👋 Goodbye! Have a wonderful day."

    else:
        return "🤔 Sorry, I don't understand that."


print("=" * 45)
print("🤖 Welcome to CodeAlpha Chatbot")
print("Type 'bye' to exit.")
print("=" * 45)

while True:

    message = input("\nYou : ")

    reply = chatbot_response(message)

    print("Bot :", reply)

    if message.lower() == "bye":
        break