
import os
import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
    confusion_matrix
)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, SimpleRNN, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping


# =========================================================
# Configuration
# =========================================================

DATASET_PATH = "../dataset/water_quality_dataset.csv"

MODEL_DIR = "model"

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "rnn_water_quality.keras"
)

SCALER_PATH = os.path.join(
    MODEL_DIR,
    "water_quality_scaler.pkl"
)

FEATURES = [
    "pH",
    "TDS_ppm",
    "Turbidity_NTU",
    "Temperature_C"
]

TARGET = "Label"


# =========================================================
# Load Dataset
# =========================================================

print("\nLoading dataset...")

df = pd.read_csv(DATASET_PATH)

df.columns = df.columns.str.strip()

df[TARGET] = (
    df[TARGET]
    .astype(str)
    .str.strip()
)


# =========================================================
# Encode Target
# =========================================================

df[TARGET] = df[TARGET].map({
    "Safe": 0,
    "Unsafe": 1
})


if df[TARGET].isnull().any():

    raise ValueError(
        "Dataset contains an unknown target label."
    )


# =========================================================
# Prepare Features
# =========================================================

X = df[FEATURES].apply(
    pd.to_numeric,
    errors="coerce"
)

y = df[TARGET].astype(int)


if X.isnull().any().any():

    raise ValueError(
        "Dataset contains missing or invalid feature values."
    )


print("Dataset shape:", X.shape)

print("\nClass distribution:")
print(y.value_counts())


# =========================================================
# Train-Test Split
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42,

    stratify=y
)


print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# =========================================================
# Feature Scaling
# =========================================================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(
    X_train
)

X_test_scaled = scaler.transform(
    X_test
)


# =========================================================
# Reshape for RNN
# =========================================================

# Each water-quality sample is treated as
# a sequence containing four feature timesteps.

X_train_rnn = X_train_scaled.reshape(
    X_train_scaled.shape[0],
    X_train_scaled.shape[1],
    1
)

X_test_rnn = X_test_scaled.reshape(
    X_test_scaled.shape[0],
    X_test_scaled.shape[1],
    1
)


print("\nRNN training shape:")
print(X_train_rnn.shape)

print("RNN testing shape:")
print(X_test_rnn.shape)


# =========================================================
# Build RNN Model
# =========================================================

model = Sequential([

    Input(
        shape=(
            X_train_rnn.shape[1],
            X_train_rnn.shape[2]
        )
    ),

    SimpleRNN(
        64,
        activation="tanh",
        return_sequences=True
    ),

    Dropout(0.2),

    SimpleRNN(
        32,
        activation="tanh"
    ),

    Dropout(0.2),

    Dense(
        16,
        activation="relu"
    ),

    Dense(
        1,
        activation="sigmoid"
    )
])


# =========================================================
# Compile Model
# =========================================================

model.compile(

    optimizer="adam",

    loss="binary_crossentropy",

    metrics=["accuracy"]
)


print("\nRNN model summary:\n")

model.summary()


# =========================================================
# Early Stopping
# =========================================================

early_stopping = EarlyStopping(

    monitor="val_loss",

    patience=5,

    restore_best_weights=True
)


# =========================================================
# Train Model
# =========================================================

print("\nTraining RNN...")

history = model.fit(

    X_train_rnn,

    y_train,

    validation_split=0.20,

    epochs=30,

    batch_size=64,

    callbacks=[early_stopping],

    verbose=1
)


# =========================================================
# Predictions
# =========================================================

print("\nGenerating predictions...")

y_probability = model.predict(
    X_test_rnn,
    verbose=0
).ravel()

y_prediction = (
    y_probability >= 0.5
).astype(int)


# =========================================================
# Evaluation
# =========================================================

accuracy = accuracy_score(
    y_test,
    y_prediction
)

precision = precision_score(
    y_test,
    y_prediction,
    zero_division=0
)

recall = recall_score(
    y_test,
    y_prediction,
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_prediction,
    zero_division=0
)

roc_auc = roc_auc_score(
    y_test,
    y_probability
)


print("\n====================================")
print("        RNN MODEL RESULTS")
print("====================================")

print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")
print(f"ROC-AUC  : {roc_auc:.4f}")


# =========================================================
# Classification Report
# =========================================================

print("\nClassification Report:\n")

print(
    classification_report(
        y_test,
        y_prediction,
        target_names=[
            "Safe",
            "Unsafe"
        ],
        zero_division=0
    )
)


# =========================================================
# Confusion Matrix
# =========================================================

cm = confusion_matrix(
    y_test,
    y_prediction
)

print("\nConfusion Matrix:")

print(cm)


# =========================================================
# Save Model and Scaler
# =========================================================

os.makedirs(
    MODEL_DIR,
    exist_ok=True
)

model.save(MODEL_PATH)

joblib.dump(
    scaler,
    SCALER_PATH
)


print("\n====================================")
print("Model saved successfully!")
print("====================================")

print("Model :", MODEL_PATH)
print("Scaler:", SCALER_PATH)
