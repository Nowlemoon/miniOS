import datetime
import requests
import random
import tkinter as tk
from geopy.geocoders import Nominatim

def get_weather(latitude, longitude):
    api_key = '43f6544a97e975225aad17985345b94e'  # Replace with your OpenWeatherMap API key

    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
    response = requests.get(url)
    data = response.json()

    temperature = data['main']['temp']
    temperature = round(temperature - 273.15, 2)  # Convert temperature from Kelvin to Celsius

    return temperature

def get_location():
    geolocator = Nominatim(user_agent="your-app-name")  # Replace "your-app-name" with your app name

    try:
        location = geolocator.geocode("")
        latitude = location.latitude
        longitude = location.longitude
    except:
        latitude = 0.0  # Default latitude value
        longitude = 0.0  # Default longitude value

    return latitude, longitude

def play_hangman():
    words = ['python', 'hangman', 'game', 'programming', 'computer']
    word = random.choice(words)
    guesses = ''
    tries = 6

    def guess_letter():
        nonlocal word, guesses, tries
        letter = guess_entry.get().lower()
        guess_entry.delete(0, tk.END)

        if not letter.isalpha():
            return

        if letter in guesses:
            return

        guesses += letter

        if letter not in word:
            tries -= 1

        hangman_text.set(get_hangman_text())

        if tries == 0 or all(letter in guesses for letter in word):
            guess_button.config(state=tk.DISABLED)

    def get_hangman_text():
        return ' '.join(letter if letter in guesses else '_' for letter in word)

    hangman_window = tk.Toplevel(root)
    hangman_window.title("Hangman Game")

    hangman_text = tk.StringVar()
    hangman_label = tk.Label(hangman_window, textvariable=hangman_text, font=('Arial', 20))
    hangman_label.pack(pady=10)

    guess_label = tk.Label(hangman_window, text="Guess a letter:")
    guess_label.pack()

    guess_entry = tk.Entry(hangman_window)
    guess_entry.pack()

    guess_button = tk.Button(hangman_window, text="Guess", command=guess_letter)
    guess_button.pack(pady=10)

    def update_hangman_text():
        hangman_text.set(get_hangman_text())
        if tries == 0 or all(letter in guesses for letter in word):
            guess_button.config(state=tk.DISABLED)
        else:
            guess_button.config(state=tk.NORMAL)

    update_hangman_text()

def exit_app():
    root.destroy()

def update_time():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_label.config(text=f"Date is: {current_time}")
    time_label.after(1000, update_time)

def update_weather(latitude, longitude):
    temperature = get_weather(latitude, longitude)
    weather_label.config(text=f"The temperature is: {temperature}°C")
    weather_label.after(60000, lambda: update_weather(latitude, longitude))

root = tk.Tk()
root.title("Terminal App GUI")

# Mini taskbar at the top
taskbar_frame = tk.Frame(root, bg='black', height=30)
taskbar_frame.pack(fill='x')

power_off_button = tk.Button(taskbar_frame, text="Power Off", bg='red', fg='white', command=exit_app)
power_off_button.pack(side='right')

# Hangman label in the upper-left corner
hangman_label = tk.Label(root, text="Hangman game")
hangman_label.pack(anchor='nw', padx=10, pady=10)

# Taskbar at the bottom
date_frame = tk.Frame(root, bg='black', height=30)
date_frame.pack(fill='x', side='bottom')

time_label = tk.Label(date_frame, text="Date is: ")
time_label.pack(side='left')

weather_label = tk.Label(date_frame, text="The temperature is: ")
weather_label.pack(side='right')

play_hangman_button = tk.Button(root, text="Play Hangman", command=play_hangman)
play_hangman_button.pack()

latitude, longitude = get_location()
update_time()
update_weather(latitude, longitude)

root.mainloop()
