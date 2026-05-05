# Temperature Converter CLI

A simple and interactive command-line application written in Python for converting temperatures between Celsius, Fahrenheit, and Kelvin.

The program provides a clean user interface, validates input, and demonstrates a modular and maintainable code structure.

---

## Features

- Convert between:
  - Celsius ↔ Fahrenheit
  - Celsius ↔ Kelvin
  - Fahrenheit ↔ Kelvin
- Interactive command-line menu
- Input validation using `try/except`
- Clean and modular code design

## Usage

Run the program using:

    python main.py  


## You will see a menu like this:

Available options:  
1: Celsius → Fahrenheit  
2: Fahrenheit → Celsius  
3: Kelvin → Celsius  
4: Celsius → Kelvin  
5: Kelvin → Fahrenheit  
6: Fahrenheit → Kelvin  
0: Exit  

---  

## Example
Choose: 4  
Enter temperature in Celsius: 25  
Result: 298.15 Kelvin  

---

## Project Structure

    .  
    ├── main.py  
    ├── README.md  
    └── .gitignore  
---

## How It Works
- The program uses separate functions for each conversion:  
    - celsius_to_fahrenheit  
    - fahrenheit_to_celsius  
    - celsius_to_kelvin  
    - kelvin_to_celsius  
- More complex conversions are built by combining basic ones  
- A dictionary (actions) maps user choices to functions  
- Input is validated to prevent crashes  
- The program runs in a loop until the user exits  

---

## Concepts Used

- Functional programming (conversion functions)
- Dictionary-based function mapping
- Input validation and error handling
- Separation of logic from input/output
- Code reuse (composition of conversion functions)
---

## Requirements

* Python 3.x

---

## Changelog

* feat: support Kelvin conversions (C↔K, F↔K)
    - Add Kelvin conversion functions
    - Extend CLI menu options
    - Improve coverage of temperature units  
* feat: add temperature conversion CLI
    - Add conversion functions for Celsius and Fahrenheit
    - Implement interactive menu using dictionary
    - Handle invalid input using try/except
* initial project setup
    - Initialize repository
    - Add base project files
---

## Author

Ahmad Kitana

---

## Future Improvements

- Add validation for physical constraints (e.g., Kelvin ≥ 0)
- Support command-line arguments using argparse
- Add unit tests
- Convert project into installable CLI tool
