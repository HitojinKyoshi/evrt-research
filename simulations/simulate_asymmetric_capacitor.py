import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eps0 = 8.854187817e-12
gap = 0.02
area = 0.0025
volume = area * gap
L = gap

V = np.linspace(1, 30000, 300)
E = V / gap
u = 0.5 * eps0 * E**2

asymmetry_factor = 0.02
F_electrostatic = asymmetry_factor * 0.5 * eps0 * E**2 * area

ehd_gain = 2.0e-12
F_EHD_air = ehd_gain * V**2

chi_eff = 1e-4
F_residual = chi_eff * (u * volume / L)

F_total = F_electrostatic + F_EHD_air + F_residual

df = pd.DataFrame({
    "voltage_V": V,
    "F_electrostatic_N": F_electrostatic,
    "F_EHD_air_N": F_EHD_air,
    "F_residual_N": F_residual,
    "F_total_N": F_total
})
df.to_csv("asymmetric_capacitor_force_model.csv", index=False)

plt.figure(figsize=(8, 5))
plt.plot(V/1000, F_electrostatic, label="Electrostatic")
plt.plot(V/1000, F_EHD_air, label="EHD air")
plt.plot(V/1000, F_residual, label="Residual chi_eff")
plt.plot(V/1000, F_total, label="Total")
plt.xlabel("Voltage (kV)")
plt.ylabel("Force (N)")
plt.yscale("log")
plt.title("Asymmetric Capacitor Reduced-Order Force Model")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("force_vs_voltage.png", dpi=200)
plt.show()
