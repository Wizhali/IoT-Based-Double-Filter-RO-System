
from flask import Flask, request, jsonify
import os
import numpy as np
import joblib

from tensorflow.keras.models import load_model


# =========================================================
# Flask Application
# =========================================================

app = Flask(__name__)


# =========================================================
# Model Paths
# =========================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "machine-learning",
    "model",
    "rnn_water_quality.keras"
)

SCALER_PATH = os.path.join(
    BASE_DIR,
    "..",
    "machine-learning",
    "model",
    "water_quality_scaler.pkl"
)


# =========================================================
# Load Model and Scaler
# =========================================================

print("Loading RNN model...")

model = load_model(MODEL_PATH)

scaler = joblib.load(SCALER_PATH)

print("RNN model loaded successfully.")


# =========================================================
# Home Route
# =========================================================

@app.route("/")
def home():

    return jsonify({
        "project": "IoT-Based Double-Filter RO System",
        "status": "Backend running",
        "model": "RNN Water Quality Classifier"
    })


# =========================================================
# Water Quality Prediction
# =========================================================

@app.route(
    "/api/predict",
    methods=["POST"]
)
def predict():

    try:

        data = request.get_json()

        # ---------------------------------------------
        # Read sensor values
        # ---------------------------------------------

        ph = float(data["ph"])

        tds = float(data["tds"])

        turbidity = float(
            data["turbidity"]
        )

        temperature = float(
            data["temperature"]
        )

        # ---------------------------------------------
        # Prepare input
        # ---------------------------------------------

        input_data = np.array([
            [
                ph,
                tds,
                turbidity,
                temperature
            ]
        ])

        # ---------------------------------------------
        # Scale input
        # ---------------------------------------------

        input_scaled = scaler.transform(
            input_data
        )

        # ---------------------------------------------
        # Reshape for RNN
        # ---------------------------------------------

        input_rnn = input_scaled.reshape(
            input_scaled.shape[0],
            input_scaled.shape[1],
            1
        )

        # ---------------------------------------------
        # Prediction
        # ---------------------------------------------

        probability = float(
            model.predict(
                input_rnn,
                verbose=0
            )[0][0]
        )

        # ---------------------------------------------
        # Classification
        # ---------------------------------------------

        if probability >= 0.5:

            label = "Unsafe"

        else:

            label = "Safe"

        # ---------------------------------------------
        # Response
        # ---------------------------------------------

        return jsonify({

            "status": "success",

            "water_quality": label,

            "unsafe_probability": round(
                probability,
                4
            ),

            "sensor_data": {

                "pH": ph,

                "TDS_ppm": tds,

                "Turbidity_NTU": turbidity,

                "Temperature_C": temperature

            }

        })


    except KeyError as error:

        return jsonify({

            "status": "error",

            "message": (
                f"Missing parameter: {error}"
            )

        }), 400


    except Exception as error:

        return jsonify({

            "status": "error",

            "message": str(error)

        }), 500


# =========================================================
# Health Check
# =========================================================

@app.route(
    "/api/health",
    methods=["GET"]
)
def health():

    return jsonify({

        "status": "online",

        "model_loaded": True

    })


# =========================================================
# Run Application
# =========================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
