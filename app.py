
import streamlit as st
import requests

API_KEY = "0e8d2bd6dd705add9fd0e07223f722c6"
BASE_URL = "http://data.fixer.io/api/"

# Fetch symbols
@st.cache_data
def get_symbols():
    url = f"{BASE_URL}symbols?access_key={API_KEY}"
    data = requests.get(url).json()
    if data.get("success"):
        return data["symbols"]
    return {}

# Fetch rate
def get_rate(base, target):
    url = f"{BASE_URL}latest?access_key={API_KEY}&symbols={base},{target}"
    data = requests.get(url).json()
    if data.get("success"):
        rates = data["rates"]
        if base == "EUR":
            return rates[target]
        elif target == "EUR":
            return 1 / rates[base]
        else:
            return rates[target] / rates[base]
    return None

# Convert amount
def convert(base, target, amount):
    rate = get_rate(base, target)
    if rate:
        return amount * rate
    return None

# --- Streamlit UI ---
st.title("💱 Currency Converter")

symbols = get_symbols()
if not symbols:
    st.error("Failed to fetch currency symbols. Check API key.")
else:
    st.subheader("Convert Currencies")
    col1, col2 = st.columns(2)

    with col1:
        base = st.selectbox("Base Currency", list(symbols.keys()))
    with col2:
        target = st.selectbox("Target Currency", list(symbols.keys()))

    amount = st.number_input(f"Amount in {base}", min_value=0.0, value=1.0, step=1.0)

    if st.button("Convert"):
        result = convert(base, target, amount)
        if result:
            st.success(f"{amount} {base} = {result:.2f} {target}")
        else:
            st.error("Failed to convert currency.")
