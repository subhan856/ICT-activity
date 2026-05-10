import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Mechanical Unit Converter",
    page_icon="⚙️",
    layout="centered"
)

# Title
st.title("⚙️ Mechanical Unit Converter & Material Density Checker")

# Student Information
st.markdown("### Developed By")
st.write("**Name:** Muhammad Subhan Babar")
st.write("**Roll Number:** 25-ME-195")

st.markdown("---")

# =========================
# UNIT CONVERTER SECTION
# =========================

st.header("🔄 Mechanical Unit Converter")

conversion_type = st.selectbox(
    "Select Conversion Type",
    ["Length", "Mass", "Temperature"]
)

# Length Converter
if conversion_type == "Length":

    meter = st.number_input("Enter value in Meters", min_value=0.0)

    centimeter = meter * 100
    millimeter = meter * 1000
    feet = meter * 3.28084

    st.success(f"Centimeters: {centimeter:.2f} cm")
    st.success(f"Millimeters: {millimeter:.2f} mm")
    st.success(f"Feet: {feet:.2f} ft")

# Mass Converter
elif conversion_type == "Mass":

    kg = st.number_input("Enter value in Kilograms", min_value=0.0)

    grams = kg * 1000
    pounds = kg * 2.20462

    st.success(f"Grams: {grams:.2f} g")
    st.success(f"Pounds: {pounds:.2f} lbs")

# Temperature Converter
elif conversion_type == "Temperature":

    celsius = st.number_input("Enter Temperature in Celsius")

    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15

    st.success(f"Fahrenheit: {fahrenheit:.2f} °F")
    st.success(f"Kelvin: {kelvin:.2f} K")

st.markdown("---")

# =========================
# MATERIAL DENSITY CHECKER
# =========================

st.header("🧱 Material Density Checker")

materials = {
    "Steel": 7850,
    "Aluminum": 2700,
    "Copper": 8960,
    "Brass": 8500,
    "Cast Iron": 7200
}

selected_material = st.selectbox(
    "Select Material",
    list(materials.keys())
)

density = materials[selected_material]

st.info(f"Density of {selected_material}: {density} kg/m³")

st.markdown("---")

# Footer
st.caption("Mechanical Engineering Mini Project using Streamlit")
