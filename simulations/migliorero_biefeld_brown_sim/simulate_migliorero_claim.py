import numpy as np
import pandas as pd

eps0 = 8.854187817e-12
g = 9.80665
k_musha = 8.62e-11

diameter = 4.0
area = np.pi * (diameter/2)**2
thickness = 0.001
density = 5200
Z = 23.33
er = 13500
V = 100000

E = V / thickness
volume = area * thickness
mass = volume * density

Eg = k_musha * Z * np.sqrt(er) * E
F_musha = mass * Eg

pressure = 0.5 * eps0 * er * E**2
F_internal_pressure = pressure * area

chi_eff = 1e-4
F_residual = chi_eff * (pressure * volume / thickness)

print("Mass (kg):", mass)
print("Electric field (V/m):", E)
print("Migliorero/Musha force (N):", F_musha)
print("Migliorero/Musha force (kgf):", F_musha / g)
print("Internal electrostatic pressure scale (N):", F_internal_pressure)
print("Internal electrostatic pressure scale (kgf):", F_internal_pressure / g)
print("EVRT residual chi_eff=1e-4 (N):", F_residual)
print("EVRT residual chi_eff=1e-4 (kgf):", F_residual / g)
