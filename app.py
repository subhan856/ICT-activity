import streamlit as st
import math

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="MECHNIX Pro",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.main {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}

h1, h2, h3, h4 {
    color: #00d4ff;
}

.stButton>button {
    background-color: #00d4ff;
    color: black;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
}

.stSelectbox label,
.stNumberInput label {
    color: white !important;
    font-size: 18px;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

col1, col2 = st.columns([1,4])

with col1:
    st.image("uet_logo.png", width=130)

with col2:
    st.title("⚙️ MECHNIX Pro")
    st.subheader("Mechanical Engineering Toolkit")
    st.write("Developed By: Muhammad Subhan Babar")
    st.write("Roll Number: 25-ME-195")
    st.write("UET Taxila")

st.markdown("---")

# =========================
# SIDEBAR
# =========================

st.sidebar.title("⚙️ Navigation")

menu = st.sidebar.selectbox(
    "Select Tool",
    [
        "Mechanical Unit Converter",
        "Material Density Checker",
        "Scientific Calculator"
    ]
)

# =========================
# SCIENTIFIC CALCULATOR
# =========================

if menu == "Scientific Calculator":

    st.header("🔬 Scientific Calculator")

    number = st.number_input("Enter Number", value=1.0)

    operation = st.selectbox(
        "Choose Operation",
        [
            "Square Root",
            "Square",
            "Cube",
            "Sin",
            "Cos",
            "Tan",
            "Log",
            "Factorial"
        ]
    )

    try:

        if operation == "Square Root":
            result = math.sqrt(number)

        elif operation == "Square":
            result = number ** 2

        elif operation == "Cube":
            result = number ** 3

        elif operation == "Sin":
            result = math.sin(math.radians(number))

        elif operation == "Cos":
            result = math.cos(math.radians(number))

        elif operation == "Tan":
            result = math.tan(math.radians(number))

        elif operation == "Log":
            result = math.log10(number)

        elif operation == "Factorial":
            result = math.factorial(int(number))

        st.success(f"Result = {result}")

    except:
        st.error("Invalid Input")

# =========================
# UNIT CONVERTER
# =========================

elif menu == "Mechanical Unit Converter":

    st.header("📏 Mechanical Unit Converter")

    conversion = st.selectbox(
        "Choose Quantity",
        [
            "Length",
            "Mass",
            "Temperature",
            "Pressure",
            "Velocity",
            "Acceleration",
            "Force",
            "Energy",
            "Power",
            "Torque",
            "Area",
            "Volume",
            "Density",
            "Frequency",
            "Time"
        ]
    )

    # LENGTH
    if conversion == "Length":

        meter = st.number_input("Enter Meter")

        st.success(f"Centimeter = {meter * 100:.2f} cm")
        st.success(f"Millimeter = {meter * 1000:.2f} mm")
        st.success(f"Feet = {meter * 3.28084:.2f} ft")
        st.success(f"Inch = {meter * 39.37:.2f} in")

    # MASS
    elif conversion == "Mass":

        kg = st.number_input("Enter Kilogram")

        st.success(f"Gram = {kg * 1000:.2f} g")
        st.success(f"Pounds = {kg * 2.20462:.2f} lbs")

    # TEMPERATURE
    elif conversion == "Temperature":

        c = st.number_input("Enter Celsius")

        st.success(f"Fahrenheit = {(c * 9/5)+32:.2f} °F")
        st.success(f"Kelvin = {c + 273.15:.2f} K")

    # PRESSURE
    elif conversion == "Pressure":

        pa = st.number_input("Enter Pascal")

        st.success(f"Bar = {pa / 100000:.4f} bar")
        st.success(f"PSI = {pa / 6895:.4f} psi")

    # VELOCITY
    elif conversion == "Velocity":

        ms = st.number_input("Enter m/s")

        st.success(f"km/h = {ms * 3.6:.2f}")
        st.success(f"mph = {ms * 2.237:.2f}")

    # ACCELERATION
    elif conversion == "Acceleration":

        acc = st.number_input("Enter m/s²")

        st.success(f"ft/s² = {acc * 3.281:.2f}")

    # FORCE
    elif conversion == "Force":

        force = st.number_input("Enter Newton")

        st.success(f"kN = {force / 1000:.2f}")
        st.success(f"lbf = {force * 0.2248:.2f}")

    # ENERGY
    elif conversion == "Energy":

        joule = st.number_input("Enter Joule")

        st.success(f"kJ = {joule / 1000:.2f}")
        st.success(f"calories = {joule * 0.239:.2f}")

    # POWER
    elif conversion == "Power":

        watt = st.number_input("Enter Watt")

        st.success(f"kW = {watt / 1000:.2f}")
        st.success(f"Horsepower = {watt * 0.00134:.2f}")

    # TORQUE
    elif conversion == "Torque":

        torque = st.number_input("Enter Nm")

        st.success(f"lb-ft = {torque * 0.73756:.2f}")

    # AREA
    elif conversion == "Area":

        area = st.number_input("Enter m²")

        st.success(f"cm² = {area * 10000:.2f}")
        st.success(f"ft² = {area * 10.764:.2f}")

    # VOLUME
    elif conversion == "Volume":

        vol = st.number_input("Enter m³")

        st.success(f"Liters = {vol * 1000:.2f}")
        st.success(f"ft³ = {vol * 35.315:.2f}")

    # DENSITY
    elif conversion == "Density":

        density = st.number_input("Enter kg/m³")

        st.success(f"g/cm³ = {density / 1000:.4f}")

    # FREQUENCY
    elif conversion == "Frequency":

        hz = st.number_input("Enter Hertz")

        st.success(f"kHz = {hz / 1000:.2f}")
        st.success(f"MHz = {hz / 1_000_000:.6f}")

    # TIME
    elif conversion == "Time":

        sec = st.number_input("Enter Seconds")

        st.success(f"Minutes = {sec / 60:.2f}")
        st.success(f"Hours = {sec / 3600:.2f}")

# =========================
# DENSITY CHECKER
# =========================

elif menu == "Material Density Checker":

    st.header("🧱 Material Density Checker")

    materials = {

        "Steel":7850,
        "Aluminum":2700,
        "Copper":8960,
        "Brass":8500,
        "Titanium":4500,
        "Cast Iron":7200,
        "Gold":19300,
        "Silver":10490,
        "Lead":11340,
        "Nickel":8908,
        "Zinc":7135,
        "Magnesium":1740,
        "Concrete":2400,
        "Glass":2500,
        "Wood":700,
        "Rubber":1522,
        "Plastic":950,
        "PVC":1380,
        "Water":1000,
        "Ice":917,
        "Mercury":13534,
        "Granite":2750,
        "Marble":2560,
        "Coal":1100,
        "Petrol":737,
        "Diesel":850,
        "Air":1.225,
        "Hydrogen":0.089,
        "Oxygen":1.429,
        "Carbon Fiber":1750,
        "CFRP":1600,
        "GFRP":1850,
        "Brick":1920,
        "Sand":1600,
        "Soil":1200,
        "Bamboo":350,
        "Paper":1200,
        "Foam":75,
        "Ceramic":2400,
        "Lithium":534,
        "Platinum":21450,
        "Uranium":19050,
        "Tungsten":19250,
        "Silicon":2330,
        "Asphalt":2243,
        "Soap":900,
        "Milk":1035,
        "Oil":920,
        "Salt":2160,
        "Sugar":1590

    }

    material = st.selectbox(
        "Select Material",
        list(materials.keys())
    )

    st.success(f"Density of {material} = {materials[material]} kg/m³")

# =========================
# FOOTER
# =========================

st.markdown("---")

st.markdown("""
<center>
<h4 style='color:#00d4ff'>
⚙️ MECHNIX Pro | UET Taxila
</h4>
</center>
""", unsafe_allow_html=True)
