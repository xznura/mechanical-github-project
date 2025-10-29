# src/beam_deflection.py
"""
Simple calculation of beam deflection for a simply supported beam.
Requirements: Python3, numpy, matplotlib
Install: pip install numpy matplotlib
"""
import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 1.0        # length of the beam, m
P = 100.0      # central point load, N
E = 210e9      # Young's modulus for steel, Pa
b = 0.02       # section width, m
h = 0.005      # section height, m

# second moment of area for rectangular section
I = b * h**3 / 12.0

# analytical max deflection for central point load
delta_max = P * L**3 / (48.0 * E * I)
print(f"Max deflection (center) = {delta_max*1000:.4f} mm")

# Example: deflection curve for uniformly distributed load q
q = 1000.0  # N/m (example)
x = np.linspace(0, L, 200)
# deflection w(x) for simply supported beam under uniform load q
w = (q * x * (L**3 - 2*L*x**2 + x**3)) / (24.0 * E * I)

plt.figure()
plt.plot(x, w*1000)
plt.xlabel('x, m')
plt.ylabel('deflection, mm')
plt.title('Deflection for uniformly distributed load q')
plt.grid(True)
plt.savefig('Results/plots.png', bbox_inches='tight')
plt.show()
