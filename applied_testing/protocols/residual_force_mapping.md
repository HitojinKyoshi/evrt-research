# Residual Force Mapping Protocol

## Objective

To determine whether an asymmetric electromagnetic test article produces a repeatable, geometry-dependent residual force that survives standard artifact rejection controls.

## Experimental Setup

- asymmetric plate configuration (3"x3" and 1"x1")
- low-voltage power source (12–24V)
- series resistor (10Ω / 20Ω)
- low-friction platform or precision scale
- temperature monitoring
- fixed cable routing with strain relief
- level surface

## Test Sequence

### 1. Baseline

- device unpowered
- record drift for 10–15 minutes

### 2. Power-On Test

- apply voltage
- record position/force over time
- record temperature

### 3. Power-Off

- remove power
- observe relaxation behavior

### 4. Orientation Mapping

Repeat tests at:

- 0°
- 90°
- 180°
- 270°

## Control Tests

### Dummy Load

- remove plates
- run resistor only

### Symmetric Configuration

- replace with equal-sized plates

### Cable Control

- vary cable position
- confirm no directional bias

### Thermal Check

- compare temperature vs motion

## Data Recording

Minimum dataset:

```csv
time,orientation,voltage,current,temp,position,notes
