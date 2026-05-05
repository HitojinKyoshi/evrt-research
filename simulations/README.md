# EVRT Reduced-Order Simulation

This package models an asymmetric high-voltage capacitor using three components:

F_total = F_electrostatic + F_EHD + F_residual

Where:
- F_electrostatic is a conservative electrostatic field-pressure/asymmetry component.
- F_EHD is an illustrative pressure-dependent electrohydrodynamic artifact term.
- F_residual is an EVRT-style effective response term: F_residual ~ chi_eff * (u V / L).

This is not a calibrated physical prediction. It is a screening model for asking:
"How large would chi_eff need to be after ordinary artifacts are accounted for?"
