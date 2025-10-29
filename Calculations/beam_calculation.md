# Beam Deflection Calculation (Central Point Load)

**Given Parameters:**
- **L** (Length of the beam): $1.0 \, \text{m}$
- **P** (Central point load): $100 \, \text{N}$
- **b** (Section width): $0.02 \, \text{m}$
- **h** (Section height): $0.005 \, \text{m}$
- **E** (Young's Modulus for steel): $210 \times 10^9 \, \text{Pa}$

---

### 1. Calculation of the Second Moment of Area (Moment of Inertia)

The formula for the moment of inertia ($I$) for a rectangular cross-section is:
$$I = \frac{b h^3}{12}$$

Substituting the values:
$$I = \frac{0.02 \, \text{m} \times (0.005 \, \text{m})^3}{12} = 2.0833333 \times 10^{-10} \, \text{m}^4$$

---

### 2. Calculation of Maximum Deflection

The formula for the maximum deflection ($\delta_{\max}$) of a simply supported beam with a central point load ($P$) is:
$$\delta_{\max} = \frac{P L^3}{48 E I}$$

Substituting the values:
$$\delta_{\max} = \frac{100 \, \text{N} \times (1.0 \, \text{m})^3}{48 \times (210 \times 10^9 \, \text{Pa}) \times (2.0833333 \times 10^{-10} \, \text{m}^4)} \approx 0.047619 \, \text{m}$$

Converting to millimeters (mm):
$$\delta_{\max} \approx 47.619 \, \text{mm}$$

---

### Conclusion

The maximum deflection calculated for the chosen geometry and load is approximately **$47.6 \, \text{mm}$**. This deflection is quite large for a $1 \, \text{m}$ long beam with such small cross-sectional dimensions. To reduce the deflection, one should consider increasing the section height ($h$) which dramatically increases the moment of inertia, reducing the span ($L$), or utilizing a material with a higher Young's Modulus ($E$).
