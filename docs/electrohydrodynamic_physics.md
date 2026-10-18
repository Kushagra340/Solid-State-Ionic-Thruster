# ⚡ Electrohydrodynamic (EHD) Propulsion Physics & The Biefeld-Brown Effect

## 1. Townsend Avalanche & Corona Ionization
When high voltage ($V > 25\text{ kV}$) is applied to an ultra-thin wire with a microscopic radius of curvature ($r_{\text{wire}} \approx 0.05\text{ mm}$), the local electric field intensity exceeds the dielectric breakdown threshold of air:
$$E_{\text{surface}} = \frac{V}{r_{\text{wire}} \cdot \ln(d / r_{\text{wire}})} > 30\text{ kV/cm}$$
At this threshold, neutral atmospheric molecules ($N_2, O_2$) undergo field electron stripping, forming a localized violet plasma sheath of positive ions.

## 2. Momentum Transfer & Space Charge Drift
The positive ions are accelerated downward by the electrostatic field toward the smooth, grounded aluminum foil cathode skirt across gap distance $d$:
$$F_{\text{EHD}} = \frac{I \cdot d}{\mu_i}$$
where:
- $F_{\text{EHD}}$ is total electrostatic thrust (Newtons).
- $I$ is corona discharge current (Amperes, typically $0.5 - 2.0\text{ mA}$).
- $d$ is electrode separation distance (meters, typically $30 - 50\text{ mm}$).
- $\mu_i$ is ion mobility in ambient air ($\approx 1.8 \times 10^{-4}\text{ m}^2/\text{V}\cdot\text{s}$).

## 3. Specific Thrust & Efficiency Scaling
$$\text{Power } P = I \cdot V \implies \frac{F}{P} = \frac{d}{\mu_i \cdot V} = \frac{1}{\mu_i \cdot E_{\text{avg}}}$$
Notice that specific thrust (Newtons per Watt) is inversely proportional to average electric field, meaning larger electrode gaps operate with superior energy efficiency.
