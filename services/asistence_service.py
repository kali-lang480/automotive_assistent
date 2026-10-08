def detect_intent(message):
    message = message.lower()

    if any(word in message for word in [
        "risk", "safe", "safety", "danger"
    ]):
        return "SAFETY"

    if any(word in message for word in [
        "alert", "warning", "problem"
    ]):
        return "ALERTS"

    if any(word in message for word in [
        "route",
        "navigate",
        "navigation",
        "direction",
        "take me",
        "go to",
        "get me to",
        "drive me",
        "nearest hospital",
        "nearest",
        "destination"
    ]):
        return "NAVIGATION"

    if any(word in message for word in [
        "vehicle", "car", "health", "condition", "status"
    ]):
        return "VEHICLE_HEALTH"

    return "GENERAL"

def extract_destination(message):
    message = message.strip()

    prefixes = [
        "take me to ",
        "go to ",
        "get me to ",
        "drive me to ",
        "navigate to ",
        "route to "
    ]

    message_lower = message.lower()

    for prefix in prefixes:
        if message_lower.startswith(prefix):
            return message[len(prefix):].strip()

    return message

def generate_response(
    intent,
    health=None,
    safety=None,
    alerts=None,
    navigation=None
):
    if intent == "VEHICLE_HEALTH":
        score = health["health_score"]
        status = health["overall_status"]

        if health["warnings"]:
            warnings = ", ".join(health["warnings"])
            return (
                f"Your vehicle health is {status.lower()} "
                f"with a score of {score}%. {warnings}"
            )

        return (
            f"Your vehicle is {status.lower()} "
            f"with a health score of {score}%."
        )

    if intent == "SAFETY":
        if safety["risks"]:
            risks = ", ".join(safety["risks"])
            return (
                f"Current safety risk is "
                f"{safety['risk_level'].lower()}. {risks}"
            )

        return "Your vehicle is currently operating safely."

    if intent == "ALERTS":
        if alerts:
            messages = ", ".join(
                alert["message"] for alert in alerts
            )
            return (
                f"There are {len(alerts)} active alerts. "
                f"{messages}"
            )

        return "There are currently no active alerts."

    if intent == "NAVIGATION":
        if navigation:
            return (
                f"Route to {navigation['destination']} "
                f"is {navigation['distance_km']} km "
                f"and will take approximately "
                f"{navigation['estimated_time_minutes']} minutes."
            )

        return "Please provide a destination."

    return (
        "I can help with vehicle health, safety, "
        "alerts, and navigation."
    )