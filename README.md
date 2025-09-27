# Currency Converter

A simple Python-based currency converter that allows you to:

- List supported currencies
- Check exchange rates between currencies
- Convert amounts from one currency to another

This project uses [Fixer.io](https://fixer.io) API for real-time currency data.

---

## Features

- Console-based interactive interface
- Input validation for currency codes and amounts
- Conversion between any two supported fiat currencies
- Optimized to handle free Fixer.io restrictions by using EUR as intermediary
- Clear instructions for available commands: `list`, `rate`, `convert`, `q` (quit)

---

## Commands

- `list` → List all supported currencies  
- `rate` → Get exchange rate between two currencies  
- `convert` → Convert amount from one currency to another  
- `q` → Quit the program  

---

## Fixer.io Limitations

- Free Fixer.io accounts **only allow EUR as the base currency**.
- Direct conversions using other bases (USD, NPR, GBP, etc.) are **not allowed** on the free plan.
- To work around this, this program **calculates all conversions via EUR** internally, so you can still convert between any supported currency.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/currency-converter-gui.git
cd currency-converter

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

3. Install dependencies:
```bash
pip install -r requirements.txt


4. Replace API_KEY in main.py with your own Fixer.io API key.

**Run the program:**
python main.py
