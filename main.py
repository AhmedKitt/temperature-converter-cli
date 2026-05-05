def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9

def kelvin_to_celsius(kelvin: float) -> float:
    return kelvin - 273.15

def celsius_to_kelvin(celsius: float) -> float:
    return celsius + 273.15

def kelvin_to_fahrenheit(kelvin: float) -> float:
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)


actions = {
    1: {
        "label": "Celsius → Fahrenheit",
        "func": celsius_to_fahrenheit,
        "in_unit": "Celsius",
        "out_unit": "Fahrenheit"
    },
    2: {
        "label": "Fahrenheit → Celsius",
        "func": fahrenheit_to_celsius,
        "in_unit": "Fahrenheit",
        "out_unit": "Celsius"
    },
    3: {
        "label": "Kelvin → Celsius",
        "func": kelvin_to_celsius,
        "in_unit": "Kelvin",
        "out_unit": "Celsius"
    },
    4: {
        "label": "Celsius → Kelvin",
        "func": celsius_to_kelvin,
        "in_unit": "Celsius",
        "out_unit": "Kelvin"
    },
    5: {
        "label": "Kelvin → Fahrenheit",
        "func": kelvin_to_fahrenheit,
        "in_unit": "Kelvin",
        "out_unit": "Fahrenheit"
    },
    6: {
        "label": "Fahrenheit → Kelvin",
        "func": fahrenheit_to_kelvin,
        "in_unit": "Fahrenheit",
        "out_unit": "Kelvin"
    },
    0: {
        "label": "Exit",
        "func": None
    }
}


def get_choice(actions_dict):
    while True:
        print("\nAvailable options:")
        for key, action in actions_dict.items():
            print(f"{key}: {action['label']}")

        try:
            choice = int(input("Choose: "))
            if choice in actions_dict:
                return choice
            print("Invalid option. Try again.")
        except ValueError:
            print("Please enter a number.")


def get_temperature(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Try again.")

def main():
    while True:
        choice = get_choice(actions)
        action = actions[choice]

        if action["func"] is None:
            print("Goodbye.")
            break

        temp = get_temperature(f"Enter temperature in {action['in_unit']}: ")
        result = action["func"](temp)

        print(f"Result: {result:.2f} {action['out_unit']}")

if __name__ == "__main__":
    main()