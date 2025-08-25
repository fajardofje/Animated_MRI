import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Constants
p0 = 1  # Assume unit spin excess probability for simplicity
gamma = 2.675e8  # Gyromagnetic ratio for proton in rad/s/T
h = 6.626e-34  # Planck's constant in J*s
K = 1.381e-23  # Boltzmann constant in J/K

# Streamlit UI
st.title("Magnetization Visualization")
st.write("""
This app visualizes the magnetization equation:

$$M_0 = rac{p_0 \cdot \gamma^2 \cdot h^2 \cdot B_0}{4 \cdot K \cdot T}$$

Adjust the magnetic field strength (B₀) and temperature (T) to see how magnetization (M₀) changes.
""")

# User inputs
B0 = st.slider("Magnetic Field Strength B₀ (Tesla)", 0.5, 3.0, 1.5, 0.1)
T = st.slider("Temperature T (Kelvin)", 250, 350, 298, 1)

# Calculate M0
M0 = p0 * gamma**2 * h**2 * B0 / (4 * K * T)
st.write(f"### Calculated Magnetization M₀: {M0:.2e} (arbitrary units)")

# Plot M0 vs B0 for different temperatures
B0_values = np.linspace(0.5, 3.0, 100)
T_values = [273, 298, 310]

fig, ax = plt.subplots()
for temp in T_values:
    M0_curve = p0 * gamma**2 * h**2 * B0_values / (4 * K * temp)
    ax.plot(B0_values, M0_curve, label=f"T = {temp} K")

ax.set_title("Magnetization M₀ vs Magnetic Field B₀")
ax.set_xlabel("B₀ (Tesla)")
ax.set_ylabel("M₀ (Arbitrary Units)")
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Spin schematic
st.write("### Spin Energy Level Schematic")
num_spins = int(50 + M0 * 1e20)  # Scale M0 to get a reasonable number of spins
num_up = num_spins
num_down = 100 - num_up if num_up < 100 else 0

fig2, ax2 = plt.subplots(figsize=(6, 4))
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

# Draw energy levels
ax2.hlines(7, 1, 9, colors='blue', linewidth=2, label='Spin +1/2 (Lower Energy)')
ax2.hlines(3, 1, 9, colors='red', linewidth=2, label='Spin -1/2 (Higher Energy)')

# Draw spins
for i in range(num_up):
    ax2.plot(np.random.uniform(1, 9), np.random.uniform(7.1, 9), 'bo')
for i in range(num_down):
    ax2.plot(np.random.uniform(1, 9), np.random.uniform(1, 2.9), 'ro')

ax2.axis('off')
ax2.legend()
st.pyplot(fig2)
