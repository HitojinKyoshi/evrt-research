# EVRT/PTNEA Reduced-Order Diagnostic Simulation

This package contains a reduced-order synthetic diagnostic simulation for planning artifact-discrimination tests.

This is not a finite-element solver, not a plasma solver, and not evidence for anomalous propulsion.

Simulated diagnostics:
1. Force vs voltage / field strength
2. Force vs frequency / resonance
3. Geometry reversal
4. Pressure / vacuum sweep
5. Dummy-load response
6. Thermal-lag response

Candidate residual model:
F_residual = chi_eff * u_EM * V_active * A_geometry * resonance_gain

Artifact models include pressure-sensitive EHD/plasma behavior, delayed thermal response, dummy-load persistence, and mechanical resonance contamination.
