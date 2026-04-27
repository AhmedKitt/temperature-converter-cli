# Temperature Converter CLI

A simple and interactive command-line application written in Python for converting temperatures between Celsius and Fahrenheit.

The program provides a clean user interface, validates input, and demonstrates a modular and maintainable code structure.

---

## Features

- Convert Celsius to Fahrenheit
- Convert Fahrenheit to Celsius
- Interactive command-line menu
- Input validation using `try/except`
- Clean and modular code design

---

## Usage

Run the program using:

```bash
python main.py

You will see a menu like this:

Available options:
1: Celsius → Fahrenheit
2: Fahrenheit → Celsius
0: Exit

---

Example

Choose: 1
Enter temperature in Celsius: 25
Result: 77.00 Fahrenheit

---

Project Structure

.
├── main.py
├── README.md
└── .gitignore
---

How It Works

* The program uses separate functions for each conversion:
  * celsius_to_fahrenheit
  * fahrenheit_to_celsius
* A dictionary (actions) maps user choices to functions
* Input is validated to prevent crashes
* The program runs in a loop until the user exits

---

Concepts Used

* Functional programming (conversion functions)
* Dictionary-based function mapping
* Input validation and error handling
* Separation of logic from input/output

---

Requirements

* Python 3.x

---

Changelog

feat: add temperature conversion CLI

* Add conversion functions
* Implement interactive menu using dictionary
* Handle invalid input using try/except

initial project setup

* Initialize repository
* Add base project files

---

Author

Ahmad Kitana

---

Future Improvements

* Add more conversion
* Support command-line arguments (argparse)
* Add unit tests
* Convert project into installable CLI tool
