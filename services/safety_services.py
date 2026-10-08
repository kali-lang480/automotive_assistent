def analyze_safety(vehicle):
    risks = []
    risk_level = "LOW"

    # Overspeeding
    if vehicle["speed"] > 100:
        risks.append("Vehicle is overspeeding.")
        risk_level = "HIGH"
    elif vehicle["speed"] > 80:
        risks.append("Vehicle speed is high.")
        risk_level = "MEDIUM"

    # Engine temperature
    if vehicle["engine_temperature"] >= 120:
        risks.append("Engine temperature is critically high.")
        risk_level = "CRITICAL"
    elif vehicle["engine_temperature"] >= 105:
        risks.append("Engine temperature is high.")

    # Tyre pressure
    if vehicle["tyre_pressure"] < 25:
        risks.append("Tyre pressure is critically low.")
        risk_level = "HIGH"
    elif vehicle["tyre_pressure"] < 30:
        risks.append("Tyre pressure is low.")

    # Battery
    if vehicle["battery_voltage"] < 11.5:
        risks.append("Battery voltage is critically low.")
        risk_level = "HIGH"

    return {
        "risk_level": risk_level,
        "risks": risks
    }