import numpy as np
import matplotlib.pyplot as plt

gamma = 0.12
drive_freq = 0.98
S0 = 0.025
t_off = 15

t = np.linspace(0, 50, 4000)
dt = t[1] - t[0]

phi = np.zeros_like(t)
v = np.zeros_like(t)

for i in range(len(t) - 1):
    drive = S0 * np.cos(drive_freq * t[i]) if t[i] < t_off else 0
    a = drive - gamma * v[i] - phi[i]
    v[i + 1] = v[i] + a * dt
    phi[i + 1] = phi[i] + v[i + 1] * dt

post = t >= t_off
exp_ref = np.exp(-gamma * (t - t_off) / 2)

# Publication-style figure formatting
plt.figure(figsize=(7, 4.5))

plt.plot(
    t[post],
    exp_ref[post],
    linewidth=2.4,
    label="Maxwellian baseline"
)

plt.plot(
    t[post],
    np.abs(phi[post]) / np.max(np.abs(phi[post])),
    linewidth=2.4,
    label="EVRT response"
)

plt.xlabel("Dimensionless time", fontsize=14)
plt.ylabel("Normalized amplitude", fontsize=14)

plt.title("Ringdown Comparison", fontsize=18)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.legend(fontsize=12)

plt.tight_layout()
plt.show()
