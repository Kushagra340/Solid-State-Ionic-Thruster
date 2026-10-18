"""
Electrohydrodynamic (EHD) Thrust & Efficiency Theoretical Modeling
"""
def calculate_ehd_thrust(voltage_kv=30.0, current_ma=1.2, gap_mm=40.0):
    voltage_v = voltage_kv * 1000.0
    current_a = current_ma / 1000.0
    gap_m = gap_mm / 1000.0
    mu_i = 1.8e-4  # Ion mobility in air (m^2 / V*s)
    
    # Force in Newtons
    thrust_n = (current_a * gap_m) / mu_i
    thrust_grams = (thrust_n / 9.81) * 1000.0
    power_w = voltage_v * current_a
    specific_thrust = (thrust_n / power_w) * 1000.0  # mN / W
    
    print(f"Voltage: {voltage_kv} kV | Current: {current_ma} mA | Gap: {gap_mm} mm")
    print(f"Total Thrust: {thrust_n*1000.0:.2f} mN ({thrust_grams:.2f} grams lift)")
    print(f"Total Power: {power_w:.1f} Watts")
    print(f"Specific Thrust: {specific_thrust:.2f} mN/W")

if __name__ == "__main__":
    calculate_ehd_thrust()
