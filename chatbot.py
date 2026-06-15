# Task 4 - Basic Chatbot
def chatbot():
    print("\n🤖 Hello! I'm M.MBot. Type 'bye' to exit.\n")

    responses = {
        "hello": "Hi there! 👋 How can I help you?",
        "hi": "Hey! 😊 Nice to meet you!",
        "how are you": "I'm doing great, thanks for asking! 😄",
        "what is your name": "I'm M.MBot, your friendly chatbot! 🤖",
        "what can you do": "I can chat with you and answer simple questions!",
        "who made you": "I was created by Maham! 💻",
        "bye": "Goodbye! Have a great day! 👋",
        "thanks": "You're welcome! 😊",
        "help": "You can say: hello, how are you, bye, thanks, etc.",
    }

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "bye":
            print("M.MBot: Goodbye! Have a great day! 👋")
            break
        elif user_input in responses:
            print(f"M.MBot: {responses[user_input]}")
        else:
            print("M.MBot: Hmm, I didn't understand that. Type 'help' for options!")

chatbot()
