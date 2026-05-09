sources = {
    "thermal": 0.1,
    "vibration": 0.05,
    "laser_drift": 0.03,
    "electrostatic": 0.02
}

total = sum(sources.values())
print("Estimated uncertainty:", total)