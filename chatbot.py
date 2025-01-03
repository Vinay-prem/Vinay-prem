import random
import datetime
import pywhatkit
import webbrowser
import os
import platform
import smtplib
import psutil

# Function to respond to user input
def speak(text):
    print(f"Chatbot: {text}")

# Function for basic chatbot responses
def chatbot_response(command):
    command = command.lower()

    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you today?")
        
    elif "how are you" in command:
        speak("I'm doing great, thank you for asking!")
        
    elif "what is your name" in command:
        speak("I am your friendly chatbot assistant!")

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}.")
        
    elif "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song} on YouTube.")
        pywhatkit.playonyt(song)
    
    elif "search" in command:
        query = command.replace("search", "").strip()
        speak(f"Searching for {query}.")
        pywhatkit.search(query)

    elif "joke" in command:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't skeletons fight each other? They don't have the guts.",
            "Why don't programmers like nature? Too many bugs.",
            "How do trees access the internet? They log in."
        ]
        speak(random.choice(jokes))
    
    elif "open" in command:
        app_name = command.replace("open", "").strip().lower()
        open_application(app_name)

    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a great day!")
        exit()

    elif "weather" in command:
        speak("Sorry, I can't provide weather information at the moment, but you can check it on your browser!")
        webbrowser.open("https://weather.com")

    elif "system info" in command or "cpu" in command:
        speak(f"System Info: {platform.system()} {platform.version()} | CPU: {psutil.cpu_percent()}% usage")
    
    elif "ram" in command:
        ram = psutil.virtual_memory().percent
        speak(f"RAM Usage: {ram}%")
    
    elif "open website" in command:
        site = command.replace("open website", "").strip()
        speak(f"Opening {site}.")
        webbrowser.open(site)

    elif "send email" in command:
        speak("What is the subject of your email?")
        subject = input("Subject: ")
        speak("What is the message of your email?")
        
        message = input("Message: ")
        send_email(subject, message)

    elif "date" in command:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {today}.")

    elif "cpu usage" in command:
        cpu_usage = psutil.cpu_percent()
        speak(f"The current CPU usage is {cpu_usage}%.")
    
    elif "ram usage" in command:
        ram_usage = psutil.virtual_memory().percent
        speak(f"The current RAM usage is {ram_usage}%.")
    
    elif "shutdown" in command:
        speak("Shutting down your computer now.")
        os.system("shutdown /s /f /t 1")
    
    elif "restart" in command:
        speak("Restarting your computer now.")
        os.system("shutdown /r /f /t 1")
    
    elif "open file" in command:
        filename = command.replace("open file", "").strip()
        open_file(filename)
    
    elif "calculate" in command:
        calculate_expression(command)

    elif "goodbye" in command or "bye" in command:
        speak("Goodbye! Have a great day!")
        exit()
    
    else:
        speak("Sorry, I didn't quite understand that. Can you try again?")

# Function to open applications
def open_application(app_name):
    app_name = app_name.lower()

    if "vscode" in app_name or "visual studio code" in app_name:
        speak("Opening Visual Studio Code.")
        os.system("code")  # 'code' is the command to open VSCode
    elif "edge" in app_name or "microsoft edge" in app_name:
        speak("Opening Microsoft Edge.")
        os.system("start msedge")  # Command for Edge
    elif "idle" in app_name or "python idle" in app_name:
        speak("Opening Python IDLE.")
        os.system("python -m idlelib.idle")  # Command for Python IDLE
    elif "teams" in app_name or "microsoft teams" in app_name:
        speak("Opening Microsoft Teams.")
        os.system("start msteams")  # Command for Microsoft Teams
    elif "explorer" in app_name or "file explorer" in app_name:
        speak("Opening File Explorer.")
        os.system("explorer")  # Command for File Explorer
    elif "chrome" in app_name or "google chrome" in app_name:
        speak("Opening Google Chrome.")
        os.system("start chrome")  # Command for Chrome
    else:
        speak(f"Sorry, I don't know how to open {app_name}.")

# Function to send email
def send_email(subject, message):
    # Basic configuration for sending an email using SMTP
    sender_email = "vinaykandula970@gmail.com"
    receiver_email = "receiver_email@example.com"
    password = "your_email_password"

    msg = f"Subject: {subject}\n\n{message}"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)
        server.quit()
        speak("Email sent successfully!")
    except Exception as e:
        speak(f"Error in sending email: {e}")

# Function to open files
def open_file(filename):
    try:
        os.startfile(filename)
        speak(f"Opening {filename}.")
    except Exception as e:
        speak(f"Error opening file: {e}")

# Function to calculate expressions
def calculate_expression(command):
    try:
        expression = command.replace("calculate", "").strip()
        result = eval(expression)
        speak(f"The result of {expression} is {result}.")
    except Exception as e:
        speak(f"Error calculating the expression: {e}")

# Main loop for the chatbot
def main():
    speak("Hello, I am your chatbot assistant. Type 'exit' or 'quit' to stop.")
    
    while True:
        command = input("You: ")  # User input via typing
        chatbot_response(command)

if __name__ == "__main__":
    main()
