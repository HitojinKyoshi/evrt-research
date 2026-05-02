import pandas as pd

df = pd.read_csv("data/sample_experiment.csv")

mean_force = df["force"].mean()
std_force = df["force"].std()

print("Mean Force:", mean_force)
print("Std Dev:", std_force)

threshold = 1e-5

if abs(mean_force) < threshold:
    print("Result: Consistent with null")
else:
    print("Result: Potential signal (requires validation)")
