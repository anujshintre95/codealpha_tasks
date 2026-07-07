import random

# ==========================================
#        BASIC CHATBOT
#     CodeAlpha Internship
# ==========================================

responses = {
    "hello": [
        "👋 Hello! Nice to meet you.",
        "😊 Hi there!",
        "🙌 Hello! How can I help you today?"
    ],

    "hi": [
        "👋 Hi!",
        "😊 Hello!",
        "😄 Nice to see you!"
    ],

    "how are you": [
        "😊 I'm doing great! Thanks for asking.",
        "😁 I'm fine. Hope you're doing well too!",
        "😎 Awesome! What about you?"
    ],

    "what is your name": [
        "🤖 My name is CodeAlpha Bot.",
        "🤖 You can call me Python Bot."
    ],

    "who created you": [
        "👨‍💻 I was created using Python.",
        "🚀 I was developed as a CodeAlpha Internship Project by ANUJ SHINTRE."
    ],

    "python": [
        "🐍 Python is an easy and powerful programming language.",
        "💻 Python is widely used in AI, Web Development and Automation."
    ],

    "help": [
        """
You can ask me:

• Hello
• Hi
• How are you
• What is your name
• Who created you
• Python
• Time
• Date
• Bye
"""
    ]
}


chat_history = []


def header():

    print("=" * 50)
    print("🤖 BASIC CHATBOT")
    print("=" * 50)
    print("Type 'help' to see available commands.")
    print("Type 'bye' to exit.")
    print("=" * 50)


def chatbot(message):

    message = message.lower().strip()

    if message in responses:
        return random.choice(responses[message])

    elif message == "time":

        from datetime import datetime

        return "🕒 Current Time : " + datetime.now().strftime("%H:%M:%S")

    elif message == "date":

        from datetime import datetime

        return "📅 Today's Date : " + datetime.now().strftime("%d-%m-%Y")

    elif message in ["bye", "exit", "quit"]:

        return "👋 Goodbye! Have a wonderful day."

    else:

        return "🤔 Sorry, I don't understand that.\nType 'help'."


def main():

    header()

    while True:

        user = input("\nYou : ")

        if user.strip() == "":
            print("Bot : Please type something.")
            continue

        reply = chatbot(user)

        chat_history.append(("You", user))
        chat_history.append(("Bot", reply))

        print("\nBot :", reply)

        if user.lower() in ["bye", "exit", "quit"]:
            break

    print("\n" + "=" * 50)
    print("CHAT HISTORY")
    print("=" * 50)

    for speaker, text in chat_history:
        print(f"{speaker}: {text}")

    print("=" * 50)


if __name__ == "__main__":
    main()