def generate_alerts(vehicle, health, safety):
    alerts = []

    # Health warnings
    for warning in health["warnings"]:
        alerts.append({
            "type": "WARNING",
            "message": warning
        })

    # Safety risks
    for risk in safety["risks"]:
        alert_type = "WARNING"

        if safety["risk_level"] == "HIGH":
            alert_type = "CRITICAL"

        elif safety["risk_level"] == "CRITICAL":
            alert_type = "EMERGENCY"

        alerts.append({
            "type": alert_type,
            "message": risk
        })

    return alerts