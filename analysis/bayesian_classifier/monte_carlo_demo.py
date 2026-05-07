import numpy as np
import matplotlib.pyplot as plt

# Number of simulated experiments
N = 10000

# Simulated thermal artifact contribution
thermal_noise = np.random.normal(0, 0.02, N)

# Simulated vibration artifact contribution
vibration_noise = np.random.normal(0, 0.01, N)

# Hypothetical residual-force component
residual_signal = np.random.normal(0.03, 0.005, N)

# Total measured response
measured_force = thermal_noise + vibration_noise + residual_signal

# Plot histogram
plt.hist(measured_force, bins=100)
plt.xlabel("Measured Residual Force (arb. units)")
plt.ylabel("Counts")
plt.title("Monte Carlo Residual-Force Distribution")
plt.show()

# Simple probability threshold
threshold = 0.025

detections = measured_force > threshold

print("Detection Probability:")
print(np.mean(detections))
