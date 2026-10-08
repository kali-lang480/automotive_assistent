def calculate_vehicle_health(vehicle):
    score = 100
    warnings = []

    # Engine temperature
    temperature = vehicle["engine_temperature"]

    if temperature >= 120:
        score -= 30
        warnings.append("Engine temperature is critically high.")
    elif temperature >= 105:
        score -= 15
        warnings.append("Engine temperature is high.")

    # Battery voltage
    battery = vehicle["battery_voltage"]

    if battery < 11.5:
        score -= 20
        warnings.append("Battery voltage is critically low.")
    elif battery < 12.0:
        score -= 10
        warnings.append("Battery voltage is low.")

    # Tyre pressure
    tyre = vehicle["tyre_pressure"]

    if tyre < 25:
        score -= 20
        warnings.append("Tyre pressure is critically low.")
    elif tyre < 30:
        score -= 10
        warnings.append("Tyre pressure is slightly low.")

    # Keep score between 0 and 100
    score = max(0, min(score, 100))

    if score >= 80:
        overall = "HEALTHY"
    elif score >= 60:
        overall = "WARNING"
    else:
        overall = "CRITICAL"

    return {
        "health_score": score,
        "overall_status": overall,
        "warnings": warnings
    }