
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Store the latest water-quality reading
latest_data = {
    "ph": None,
    "tds": None,
    "turbidity": None,
    "temperature": None,
    "conductivity": None,
    "status": "No data received",
    "timestamp": None
}


# ---------------------------------------------------------
# Water Quality Evaluation
# ---------------------------------------------------------
def check_water_quality(ph, tds, turbidity, temperature):

    warnings = []

    if ph is not None and (ph < 6.5 or ph > 8.5):
        warnings.append("pH is outside the safe range")

    if tds is not None and tds > 500:
        warnings.append("TDS is above the configured limit")

    if turbidity is not None and turbidity > 5:
        warnings.append("Turbidity is above the configured limit")

    if temperature is not None and (
        temperature < 5 or temperature > 35
    ):
        warnings.append("Temperature is outside the configured range")

    if len(warnings) == 0:
        return "SAFE", warnings

    return "WARNING", warnings


# ---------------------------------------------------------
# Receive ESP32 Data
# ---------------------------------------------------------
@app.route("/api/water-data", methods=["POST"])
def receive_water_data():

    global latest_data

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "No JSON data received"
        }), 400

    try:

        ph = float(data.get("ph")) if data.get("ph") is not None else None
        tds = float(data.get("tds")) if data.get("tds") is not None else None
        turbidity = (
            float(data.get("turbidity"))
            if data.get("turbidity") is not None
            else None
        )
        temperature = (
            float(data.get("temperature"))
            if data.get("temperature") is not None
            else None
        )
        conductivity = (
            float(data.get("conductivity"))
            if data.get("conductivity") is not None
            else None
        )

        status, warnings = check_water_quality(
            ph,
            tds,
            turbidity,
            temperature
        )

        latest_data = {
            "ph": ph,
            "tds": tds,
            "turbidity": turbidity,
            "temperature": temperature,
            "conductivity": conductivity,
            "status": status,
            "warnings": warnings,
            "timestamp": datetime.now().isoformat()
        }

        print("\n---------- WATER DATA ----------")
        print(f"pH           : {ph}")
        print(f"TDS          : {tds}")
        print(f"Turbidity    : {turbidity}")
        print(f"Temperature  : {temperature}")
        print(f"Conductivity : {conductivity}")
        print(f"Status       : {status}")
        print("--------------------------------")

        return jsonify({
            "success": True,
            "message": "Water-quality data received successfully",
            "data": latest_data
        }), 200

    except (TypeError, ValueError):

        return jsonify({
            "success": False,
            "message": "Invalid sensor data"
        }), 400


# ---------------------------------------------------------
# Get Latest Water Data
# ---------------------------------------------------------
@app.route("/api/water-data", methods=["GET"])
def get_water_data():

    return jsonify(latest_data), 200


# ---------------------------------------------------------
# Health Check
# ---------------------------------------------------------
@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "project": "IoT-Based Double-Filter RO System",
        "service": "Water Quality Monitoring Backend",
        "status": "Running"
    })


# ---------------------------------------------------------
# Run Flask Server
# ---------------------------------------------------------
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
