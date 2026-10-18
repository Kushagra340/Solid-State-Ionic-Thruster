# ⚡ ZVS High-Voltage Flyback Power Supply Schematics

## Circuit Architecture
- **Driver Topology**: Zero Voltage Switching (ZVS) resonant Royer induction oscillator.
- **Power Switches**: 2× IRFP260N Power MOSFETs (50A, 200V, low $R_{DS(on)}$).
- **Transformer**: High-frequency encapsulated ferrite flyback transformer with center-tapped 5+5 turn primary winding.
- **Secondary Multiplier**: Cockcroft-Walton multi-stage cascade voltage multiplier generating 30kV DC.
- **Input Power**: 12V–24V DC, 5A–10A benchtop power supply.
