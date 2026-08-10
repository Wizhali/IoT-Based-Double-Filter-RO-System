
import os
import numpy as np
import joblib

from tensorflow.keras.models import load_model


# =========================================================
# Configuration
# =========================================================

MODEL_PATH = "model/rnn_water_quality.keras"

SCALER_PATH = "model/water_quality_scaler.pkl"


# =========================================================
# Load Model and Scaler
# =========================================================

print("Loading RNN model...")

model = load_model(MODEL_PATH)

scaler = joblib.load(SCALER_PATH)

print("Model loaded successfully.")


# =========================================================
# Prediction Function
# =========================================================

def predict_water_quality(
    ph,
    tds,
    turbidity,
    temperature
):

    # Create input array
    input_data = np.array([
        [
            ph,
            tds,
            turbidity,
            temperature
        ]
    ])

    # Apply same scaling used during training
    input_scaled = scaler.transform(
        input_data
    )

    # Reshape for RNN
    input_rnn = input_scaled.reshape(
        input_scaled.shape[0],
        input_scaled.shape[1],
        1
    )

    # Get probability
    probability = model.predict(
        input_rnn,
        verbose=0
    )[0][0]

    # Classification threshold
    if probability >= 0.5:

        label = "Unsafe"

    else:

        label = "Safe"

    return label, probability


# =========================================================
# Example Prediction
# =========================================================

if __name__ == "__main__":

    # Example sensor values
    ph = 7.38
    tds = 138.7
    turbidity = 0.25
    temperature = 20.25

    label, probability = predict_water_quality(
        ph,
        tds,
        turbidity,
        temperature
    )

    print("\n====================================")
    print("       WATER QUALITY PREDICTION")
    print("====================================")

    print(f"pH           : {ph}")
    print(f"TDS          : {tds} ppm")
    print(f"Turbidity    : {turbidity} NTU")
    print(f"Temperature  : {temperature} °C")

    print("------------------------------------")

    print(f"Prediction   : {label}")
    print(f"Probability  : {probability:.4f}")

    print("====================================")
