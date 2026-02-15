import datetime
import time
print("Welcome to your AI Study Buddy (Rule - Based Chat Assistant)")
print("You can ask me questions: ")
username = input("Enter your name : ")
current_time = datetime.datetime.now().hour
if 4 < current_time <= 11:
    print("Good Morning ", username)
elif 11 < current_time <= 16:
    print("Good Afternoon ", username)
elif 16 < current_time <= 20:
    print("Good Evening ", username)
else:
    print("Good Night ", username)

# chatbot memory creation [ dictionary of responses]
responses = {
    "hello" : "Hii, How can I help you?",
    "how are you" : "I am Fine. Thank you!!",
    "who are you" : "I am an AI Chatbot",
    "happy" : "It's awesome!! Hope you will be happy all time.",
    "sad" : "No need to stress! Everything will be Fine. Believe in God",
    "motivate me" : "You went from 'I don't know' to 'I made this'. That's real growth.",
    "what is python" : "Python is a high-level, interpreted, general-purpose programming language.",
    "uses of python" : "Python is used in AI, Machine Learning, Backend development, Data Science, Data analyst",
    "dsa in python is good or not" : "DSA in python is a great choice. You don't need to get confuse with the opinions of others."
}

def Chatbot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            # time.sleep(1)
            return responses[eachkey]
    return "I'm not able to tell that yet! I'll learn soon."
# Take user Input
while True:
    userInput = input("Please Ask your Question :- ")
    if "bye" in userInput.lower():
        print("Bye!!")
        break
    reply = Chatbot(userInput)
    print("Bot Response : ", reply)

  