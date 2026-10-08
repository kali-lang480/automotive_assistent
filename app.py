from flask import Flask, jsonify, request
from flask_cors import CORS
from services.safety_services import analyze_safety
from services.alert_service import generate_alerts
from services.asistence_service import (
    detect_intent,
    generate_response,
    extract_destination
)
from services.navigate_service import calculate_route

from services.vehicle_service import get_vehicle_data
from services.health_service import calculate_vehicle_health

app = Flask(__name__)
CORS(app)

@app.route("/api/safety/status")
def safety_status():
    vehicle = get_vehicle_data()
    safety = analyze_safety(vehicle)

    return jsonify({
        "vehicle": vehicle,
        "safety": safety
    })

@app.route("/api/alerts")
def alerts():
    vehicle = get_vehicle_data()
    health = calculate_vehicle_health(vehicle)
    safety = analyze_safety(vehicle)

    alerts = generate_alerts(vehicle, health, safety)

    return jsonify({
        "alerts": alerts
    })

@app.route("/")
def home():
    return jsonify({
        "message": "AI Vehicle Assistant Backend is running"
    })


@app.route("/api/vehicle/status")
def vehicle_status():
    vehicle = get_vehicle_data()

    return jsonify(vehicle)


@app.route("/api/vehicle/health")
def vehicle_health():
    vehicle = get_vehicle_data()
    health = calculate_vehicle_health(vehicle)

    return jsonify({
        "vehicle": vehicle,
        "health": health
    })

@app.route("/api/assistant/query", methods=["POST"])
def assistant_query():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")

    if not message:
        return jsonify({
            "error": "Message is required"
        }), 400

    intent = detect_intent(message)

    vehicle = get_vehicle_data()
    health = calculate_vehicle_health(vehicle)
    safety = analyze_safety(vehicle)
    alerts = generate_alerts(vehicle, health, safety)

    navigation = None
    if intent == "NAVIGATION":
        destination = extract_destination(message)
        navigation = calculate_route(destination)

    response = generate_response(
        intent,
        health,
        safety,
        alerts,
        navigation
    )

    return jsonify({
        "intent": intent,
        "response": response
    })

@app.route("/api/navigation/route", methods=["POST"])
def navigation_route():
    data = request.get_json()

    destination = data.get("destination", "")

    result = calculate_route(destination)

    if result["status"] == "ERROR":
        return jsonify(result), 400

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)