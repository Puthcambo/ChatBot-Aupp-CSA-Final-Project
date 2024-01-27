import tkinter as tk
from tkinter import scrolledtext
import json
from nltk.chat.util import Chat, reflections


patterns = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm fine, thanks!"]
    ],
    [
        r"What is your name?",
        ["You can call me ChatBot.", "I'm a chatbot, no specific name."]
    ],
    [
        r"(.*) your name ?",
        ["You can call me ChatBot.", "I'm a chatbot, no specific name."]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "Bye!", "See you later!"]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm a virtual chatbot, so I don't have a physical location."]
    ],
    [
        r"(.*) (weather|temperature) ?",
        ["Sorry, I can't provide real-time weather information."]
    ],
    [
        r"(.*) Are you smart ?",
        ["No, I'm not", "Surely I am not, I am still developing"]
    ],
    [
        r"(.*) (age|old) ?",
        ["I'm a virtual entity, so I don't age like humans."]
    ],
    [
        r"(.*) (love|like) (.*)",
        ["I'm just a chatbot, I don't have feelings like humans."]
    ],
    [
        r"(.*) (joke|funny) ?",
        ["Why don’t scientists trust atoms? Because they make up everything!", 
         "I told my wife she should embrace her mistakes... She gave me a hug."]
    ],
    [
        r"(.*) (movie|film) ?",
        ["I don't watch movies, but I've heard 'The Matrix' is mind-bending."]
    ],
    [
        r"(.*) (food|eat) ?",
        ["I wish I could eat! What's your favorite food?", "Food is fascinating, what's your favorite cuisine?"]
    ],
    [
        r"(.*) (music|song) ?",
        ["I don't have ears to listen, but I've heard 'Bohemian Rhapsody' is a masterpiece.",
         "Music is amazing, do you have a favorite genre?"]
    ],
    [
        r"(.*) (book|read) ?",
        ["I don't read, but '1984' by George Orwell is a classic.",
         "Books are incredible, what's your favorite book?"]
    ],
    [
        r"(.*) (sport|game) ?",
        ["I don't play sports, but chess is a fascinating game.",
         "Sports are interesting, what's your favorite sport?"]
    ],
    [
        r"(.*) (hobby|interest) ?",
        ["I'm interested in chatting with you! What about you?",
         "Hobbies are fun, what's your favorite hobby?"]
    ],
    [
        r"(.*) (technology|computer) ?",
        ["I'm a product of technology! Computers are fascinating.",
         "Technology shapes our world, what's your favorite tech gadget?"]
    ],
    [
        r"(.*) (programming|code) ?",
        ["I don't write code, but Python is a great programming language!",
         "Coding is challenging, do you have a favorite programming language?"]
    ],
    [
        r"(.*) (travel|place) ?",
        ["I haven't traveled, but I've heard Paris is beautiful.",
         "Traveling broadens horizons, do you have a favorite destination?"]
    ],
    [
        r"(.*) (animal|pet) ?",
        ["I don't have pets, but dogs are known for their loyalty.",
         "Animals are amazing, do you have a favorite animal?"]
    ],
    [
        r"(.*) (language|speak) ?",
        ["I speak many languages, but I'm most fluent in Python!", 
         "Languages are fascinating, do you speak multiple languages?"]
    ],
    [
        r"(.*) (exercise|workout) ?",
        ["I don't exercise, but staying active is important!",
         "Exercise keeps us healthy, what's your favorite workout?"]
    ],
    [
        r"(.*) (education|study) ?",
        ["I don't study, but learning is a lifelong process!",
         "Education shapes our future, what's your favorite subject?"]
    ],
    [
        r"(.*) (career|job) ?",
        ["I don't work, but finding a fulfilling career is essential!",
         "Careers are important, what's your dream job?"]
    ],
    [
        r"(.*) (nature|environment) ?",
        ["I don't experience nature, but protecting the environment is crucial!",
         "Nature is beautiful, what's your favorite outdoor activity?"]
    ],
    [
        r"(.*) (art|artist) ?",
        ["I don't create art, but art inspires creativity!",
         "Art is expressive, do you have a favorite artist?"]
    ],
    [
        r"(.*) (fashion|style) ?",
        ["I don't follow fashion, but personal style is unique!",
         "Fashion is diverse, what's your favorite clothing style?"]
    ],
    [
        r"(.*) (finance|money) ?",
        ["I don't handle money, but financial management is important!",
         "Finance is essential, what's your view on saving money?"]
    ],
    [
        r"(.*) (health|wellness) ?",
        ["I don't have health concerns, but staying healthy is vital!",
         "Health is wealth, what's your approach to a healthy lifestyle?"]
    ],
    [
        r"(.*) (relationship|partner) ?",
        ["I don't have relationships, but mutual respect is the key!",
         "Relationships are valuable, what's your ideal partner like?"]
    ],
    [
        r"(.*) (politics|government) ?",
        ["I don't engage in politics, but understanding governance is crucial!",
         "Politics influences society, what's your view on current affairs?"]
    ],
    [
        r"(.*) (science|research) ?",
        ["I don't conduct experiments, but scientific discovery is fascinating!",
         "Science is intriguing, do you have a favorite scientific theory?"]
    ],
    [
        r"(.*) (history|past) ?",
        ["I don't experience history, but learning from the past is essential!",
         "History shapes our present, do you have a favorite historical era?"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that.", "Could you please rephrase that?"]
    ]
    
]



chatbot = Chat(patterns, reflections)
def send_message():
    user_input = entry_field.get()
    if user_input.strip() != "":
        chat_area.insert(tk.END, "You: " + user_input + "\n")
        response = chatbot.respond(user_input)
        chat_area.insert(tk.END, "ChatBot: " + response + "\n\n")
        entry_field.delete(0, tk.END)

    
        save_to_json("conversation_history.json", {"user_input": user_input, "response": response})


def save_to_json(file_name, data):
    with open(file_name, 'a') as file:
        json.dump(data, file)
        file.write('\n')


def send_message():
    user_input = entry_field.get()
    if user_input.strip() != "":
        chat_area.insert(tk.END, "You: " + user_input + "\n")
        response = chatbot.respond(user_input)
        chat_area.insert(tk.END, "ChatBot: " + response + "\n\n")
        entry_field.delete(0, tk.END)

def send_message():
    user_input = entry_field.get()
    if user_input.strip() != "":
        chat_area.insert(tk.END, "You: " + user_input + "\n")
        response = chatbot.respond(user_input)
        chat_area.insert(tk.END, "ChatBot: " + response + "\n\n")
        entry_field.delete(0, tk.END)


def send_message():
    user_input = entry_field.get()
    if user_input.strip() != "":
        chat_area.insert(tk.END, "You: " + user_input + "\n")
        response = chatbot.respond(user_input)
        chat_area.insert(tk.END, "ChatBot: " + response + "\n\n")
        entry_field.delete(0, tk.END)

def send_message():
    user_input = entry_field.get()
    if user_input.strip() != "":
        chat_area.insert(tk.END, "You: " + user_input + "\n")
        response = chatbot.respond(user_input)
        chat_area.insert(tk.END, "ChatBot: " + response + "\n\n")
        entry_field.delete(0, tk.END)


root = tk.Tk()
root.title("ChatBot")
root.geometry("400x500")  


root.configure(bg="#FFB6C1")  


chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=20, bg="#FFE4E1", fg="#000000", font=("Arial", 12))
chat_area.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")


entry_field = tk.Entry(root, width=30, bg="#FFDDF4", fg="#000000", font=("Arial", 12))
entry_field.grid(row=1, column=0, padx=10, pady=10)


send_button = tk.Button(root, text="Send", command=send_message, bg="#FF69B4", fg="#ffffff", font=("Arial", 12), padx=10)
send_button.grid(row=1, column=1, padx=5, pady=10, sticky="e")


root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


root.mainloop()