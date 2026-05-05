# Migliorero / Biefeld-Brown Claim Reduced-Order Simulation

This package compares:

1. Migliorero/Musha-style linear-E force prediction
2. Conventional electrostatic internal pressure scale
3. Schematic EHD artifact pressure-dependence
4. EVRT-style residual chi_eff term

Key results:
- 4 m BST disk mass: 65.35 kg
- Claimed formula force at 100 kV / 1 mm: 155.70 kgf
- Internal electrostatic pressure scale: 765846428.48 kgf
- EVRT residual with chi_eff=1e-4: 76584.6428 kgf
- 14 cm glass example predicted by stated coefficient: 0.153 grams-force

Important:
This is not validation of the claim. It is a constraint/screening model.
The most useful discriminator is scaling:
- Claimed formula scales linearly with E / voltage.
- Conventional electrostatic pressure scales as E^2.
- EHD collapses strongly with vacuum pressure.
