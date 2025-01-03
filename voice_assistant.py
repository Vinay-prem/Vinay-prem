import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import os
import random
import subprocess

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Configure text-to-speech properties
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change to voices[1].id for a female voice
engine.setProperty('rate', 150)  # Speed of speech

# Flag to control pause/resume
paused = False

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens to user input."""
    global paused
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand. Can you say that again?")
        return ""
    except sr.RequestError:
        speak("Sorry, I'm having trouble accessing the service.")
        return ""

def tell_joke():
    """Tells a random joke."""
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "Why don't programmers like nature? Too many bugs.",
        "How do trees access the internet? They log in."
    ]
    speak(random.choice(jokes))

def handle_command(command):
    """Handles various commands."""
    global paused
    if "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song} on YouTube.")
        pywhatkit.playonyt(song)

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}.")

    elif "search for" in command:
        topic = command.replace("search for", "").strip()
        speak(f"Searching for {topic}.")
        pywhatkit.search(topic)

    elif "who is" in command or "what is" in command:
        topic = command.replace("who is", "").replace("what is", "").strip()
        info = wikipedia.summary(topic, sentences=2)
        
        speak(info)

    elif "remind me to" in command:
        task = command.replace("remind me to", "").strip()
        speak(f"Reminder set for: {task}. I will remember it.")
        # You can add this to a list or file for persistent reminders.

    elif "open" in command:
        app_name = command.replace("open", "").strip()
        open_application(app_name)

    elif "shut down" in command:
        speak("Shutting down the system. Goodbye!")
        os.system("shutdown /s /t 5")

    elif "restart" in command:
        speak("Restarting the system.")
        os.system("shutdown /r /t 5")

    elif "log off" in command:
        speak("Logging off.")
        os.system("shutdown -l")

    elif "sleep" in command:
        speak("Putting the system to sleep.")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    elif "hibernate" in command:
        speak("Putting the system into hibernation.")
        os.system("shutdown /h /f")

    elif "lock" in command:
        speak("Locking the system.")
        os.system("rundll32.exe user32.dll,LockWorkStation")

    elif "volume up" in command:
        speak("Increasing the volume.")
        subprocess.run(["nircmd.exe", "changesysvolume", "5000"])  # Uses nircmd tool to increase volume

    elif "volume down" in command:
        speak("Decreasing the volume.")
        subprocess.run(["nircmd.exe", "changesysvolume", "-5000"])  # Uses nircmd tool to decrease volume

    elif "tell me a joke" in command:
        tell_joke()

    elif "wait" in command:
        speak("Pausing. I will wait for your 'continue' command to resume.")
        paused = True

    elif "continue" in command:
        speak("Resuming.")
        paused = False

    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I'm not sure how to handle that. Can you try another command?")

def open_application(app_name):
    """Opens an application based on the command."""
    # List of common apps and their corresponding commands
    apps = {
        "notepad": "notepad",
        "calculator": "calc",
        "chrome": "start chrome",
        "word": "start winword",  # Microsoft Word
        "excel": "start excel",  # Microsoft Excel
        "paint": "mspaint",
        "file explorer": "explorer",
        "cmd": "start cmd",  # Command prompt
        "task manager": "taskmgr",
        "spotify": "start spotify"
    }

    app_name = app_name.lower()

    if app_name in apps:
        speak(f"Opening {app_name}.")
        os.system(apps[app_name])
    else:
        speak(f"Sorry, I don't know how to open {app_name}.")

# Main loop for the assistant
def main():
    speak("Hello! I am your virtual assistant. How can I help you?")
    global paused
    while True:
        if not paused:
            command = listen()
            if command:
                handle_command(command)

if __name__ == "__main__":
    main()
