# Porcelli/Filho Symmetrical Capacitor: chi_eff Mapping

Reported data modeled:
- 8 cm diameter symmetrical capacitor
- 1 mm dielectric
- mass 41.154 g
- relative permittivity ~2.65
- ~36.7 mgf at 7 kV
- up to ~220 mgf at 20 kV

EVRT residual model:
F_res = chi_eff * (u A)
where u = 0.5 eps0 eps_r E^2 and A is the plate area.

Key findings:
- Required chi_eff for 36.7 mgf at 7 kV: 1.246e-04
- Required chi_eff for 220 mgf at 20 kV: 9.146e-05
- E^2 scaling fitted to 36.7 mgf at 7 kV predicts 299.6 mgf at 20 kV.
- Reported 20 kV value is 220 mgf, so E^2 scaling is same order and actually overpredicts by factor 1.36.
- Environmental electrostatic coupling can reach mgf to tens-of-mgf levels at kV voltages for centimeter-scale distances depending on coupling fraction.

This does not validate or falsify the paper. It shows the reported values require a large effective residual parameter and are also within the range of ordinary electrostatic artifact mechanisms unless stronger isolation controls are demonstrated.
