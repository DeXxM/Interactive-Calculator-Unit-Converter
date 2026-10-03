# 🧮 Interactive Calculator & Unit Converter

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Type](https://img.shields.io/badge/Type-CLI%20App-orange)

A command-line app that combines a **calculator**, **unit converter** and **currency converter** in one simple menu.

## ✨ Features

| Module | What it does |
|---|---|
| **Arithmetic** | `+  -  *  /  %  **` with a clear error for division by zero |
| **Unit Conversion** | Length (m, km, cm, mm, inch, foot, yard, miles), weight (kg, g, mg, lb, oz) and temperature (°C, °F, K) |
| **Currency Conversion** | Converts between currencies such as INR, USD, JPY and GBP using the `CurrencyConverter` package |
| **Safe input** | Invalid numbers, operators, units and currencies show a clear message instead of crashing |

## 🚀 Getting Started

```bash
git clone https://github.com/<your-username>/calculator-unit-converter.git
cd calculator-unit-converter
pip install -r requirements.txt
python Cal_Project.py
```

> On Windows, use `py Cal_Project.py` if `python` doesn't work.
> The `pip install` step is required, because the currency feature needs the `CurrencyConverter` package.

## 🖥️ Demo

```
========================================
  Interactive Calculator & Converter
========================================
1. Arithmetic
2. Currency Conversion
3. Unit Conversion
4. Exit
Choose an option (1-4): 3

-----Unit Conversion-----
Categories: length, weight, temperature
Choose a category: length
Available units: m,km,cm,mm,inch,foot,yard,miles
Enter Value: 10
Your Value Type: km
Result Value Type: miles
Result: 10.0 km = 6.2137miles
```

## 🗂️ Project Structure

```
calculator-unit-converter/
├── Cal_Project.py     # the application
├── requirements.txt   # third-party libraries
├── README.md
└── .gitignore
```

## 📚 Python Libraries Used

| Library | Type | Purpose |
|---|---|---|
| `currency_converter` | Third-party (`pip install CurrencyConverter`) | Converts between currencies using exchange-rate data bundled with the package |

Everything else (arithmetic, unit conversion, the menu and error handling) uses only plain Python: functions, dictionaries, `input()`, `print()` and `try/except`.

## 🧠 How It Works

- **Arithmetic:** one `calculator()` function checks the operator and returns the result. Division by zero raises a clear error.
- **Unit conversion:** every value is converted to a base unit (metre or kilogram) first, then to the target unit. Adding a new unit takes one line in a dictionary.
- **Temperature:** values are converted through Celsius as a common middle step.
- **Currency:** the app creates a `CurrencyConverter()` object, checks that both currency codes are supported, then converts the amount.

## 🛣️ Roadmap

- [ ] Volume, speed and time conversions
- [ ] Expression parsing (`2 + 3 * 4`)
- [ ] Calculation history
- [ ] Unit tests with `pytest`
- [ ] Tkinter or Streamlit GUI

## 🤝 Contributing

Ideas and pull requests are welcome. Open an issue to discuss what you'd like to change.

## 👤 Author

**Devom Saini** — BCA (AI & Data Science), DY Patil University, Pune
