import re


def calculate_route(destination):
    if not isinstance(destination, str):
        return {
            "status": "ERROR",
            "message": "Destination is required."
        }

    destination = destination.strip()
    if not destination:
        return {
            "status": "ERROR",
            "message": "Destination is required."
        }

    normalized = destination.lower()
    cleaned = destination

    for prefix in [
        "navigate to ",
        "navigation to ",
        "take me to ",
        "go to ",
        "get me to ",
        "drive me to ",
        "route to ",
        "direction to "
    ]:
        if normalized.startswith(prefix):
            cleaned = destination[len(prefix):].strip()
            break
    else:
        cleaned = re.sub(
            r"(?i)\b(navigate|navigation|take me|go to|get me to|drive me|route|direction)\b",
            "",
            cleaned
        ).strip()
        if " to " in cleaned.lower():
            cleaned = cleaned.split(" to ", 1)[1].strip()

    cleaned = cleaned.strip(" ?.!;")
    if not cleaned:
        return {
            "status": "ERROR",
            "message": "Destination is required."
        }

    return {
        "status": "SUCCESS",
        "destination": cleaned,
        "distance_km": 4.8,
        "estimated_time_minutes": 12,
        "route": [
            "Start from current location",
            "Continue straight for 2 km",
            "Turn right at Main Road",
            f"Arrive at {cleaned}"
        ]
    }