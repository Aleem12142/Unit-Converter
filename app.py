import streamlit as st

# Unit categories
unit_categories = {
    "Length": ["meter", "kilometer", "centimeter", "inch", "foot", "mile"],
    "Weight": ["kilogram", "gram", "pound"],
    "Temperature": ["celsius", "fahrenheit"]
}

# Conversion dictionary
conversions = {
    "meter": {"kilometer": 0.001, "centimeter": 100, "inch": 39.37, "foot": 3.281},
    "kilometer": {"meter": 1000, "mile": 0.6214},
    "centimeter": {"meter": 0.01, "inch": 0.3937, "foot": 0.0328},
    "inch": {"centimeter": 2.54, "meter": 0.0254, "foot": 0.0833},
    "foot": {"meter": 0.3048, "inch": 12, "centimeter": 30.48},
    "mile": {"kilometer": 1.609, "meter": 1609.34},  # Added missing reverse conversion

    "kilogram": {"gram": 1000, "pound": 2.205},
    "gram": {"kilogram": 0.001},
    "pound": {"kilogram": 0.454},

    "celsius": {"fahrenheit": lambda c: round((c * 9/5) + 32, 2)},  # Rounded output
    "fahrenheit": {"celsius": lambda f: round((f - 32) * 5/9, 2)}
}

# Function to convert units
def convert(value, from_unit, to_unit):
    if from_unit in conversions and to_unit in conversions[from_unit]:
        factor = conversions[from_unit][to_unit]
        return factor(value) if callable(factor) else round(value * factor, 2)  # Ensuring clean output
    return None  # Returning None for invalid conversions

# Streamlit UI
st.title("🌍 Basic Unit Converter")

# Select category first
category = st.selectbox("📏 Select category:", list(unit_categories.keys()))

# Filter units based on category
available_units = unit_categories[category]

# User inputs
value = st.number_input("🔢 Enter a value:", min_value=0.0, step=0.1)
from_unit = st.selectbox("🔄 From unit:", available_units)
to_unit = st.selectbox("➡️ To unit:", [u for u in available_units if u != from_unit])  # Prevent same unit selection

# Convert on button click
if st.button("🚀 Convert"):
    result = convert(value, from_unit, to_unit)
    if result is not None:
        st.success(f"✅ Converted value: {result} {to_unit}")
    else:
        st.error("❌ Invalid conversion! Please check the units selected.")
