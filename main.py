import datetime
import requests
import random

def get_weather():
    # Replace 'API_KEY' with your actual API key
    api_key = '443356ddc1392c089fd3d4949a22d26b'
    city = 'Dortmund'  # Replace with the desired city

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()

    temperature = data['main']['temp']
    temperature = round(temperature - 273.15, 2)  # Convert temperature from Kelvin to Celsius

    return temperature, city

def hangman():
    words = ['python', 'hangman', 'game', 'programming', 'computer']
    word = random.choice(words)
    guesses = ''
    tries = 6

    while tries > 0:
        failed = 0

        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
                failed += 1

        if failed == 0:
            print("\nCongratulations! You guessed the word correctly.")
            break

        guess = input("\n\nGuess a letter: ")
        guesses += guess

        if guess not in word:
            tries -= 1
            print("Wrong guess!")
            print(f"You have {tries} tries left.")

        if tries == 0:
            print("\nSorry, you ran out of tries.")
            print(f"The word was '{word}'.")
            break

def calculator():
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        print("Invalid operator!")
        return

    print(f"The result is: {result}")

def main():
    while True:
        command = input("Enter a command (time, weather, hangman, calculator, exit): ")

        if command == 'time':
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"The current time is: {current_time}")
        elif command == 'weather':
            temperature, city = get_weather()
            print(f"The temperature in {city} is {temperature}°C")
        elif command == 'hangman':
            hangman()
        elif command == 'calculator':
            calculator()
        elif command == 'exit':
            break
        else:
            print("Invalid command!")

if __name__ == '__main__':
    main()