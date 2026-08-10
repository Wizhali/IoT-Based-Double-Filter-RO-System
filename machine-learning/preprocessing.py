
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# =========================================================
# Configuration
# =========================================================

DATASET_PATH = "../dataset/water_quality_dataset.csv"


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

def load_dataset():

    df = pd.read_csv(DATASET_PATH)

    print("Dataset loaded successfully")
    print("Shape:", df.shape)

    return df


# =========================================================
# Data Preprocessing
# =========================================================

def preprocess_data(df):

    # Remove unnecessary spaces from column names
    df.columns = df.columns.str.strip()

    # Remove leading/trailing spaces from labels
    df[TARGET] = df[TARGET].astype(str).str.strip()

    # Convert target labels
    df[TARGET] = df[TARGET].map({
        "Safe": 0,
        "Unsafe": 1
    })

    # Select input features
    X = df[FEATURES].copy()

    # Select target
    y = df[TARGET].copy()

    # Check for invalid target values
    if y.isnull().any():

        raise ValueError(
            "Unknown label found in dataset. "
            "Expected only 'Safe' and 'Unsafe'."
        )

    # Convert values to numeric
    X = X.apply(pd.to_numeric, errors="coerce")

    # Check missing values
    if X.isnull().any().any():

        raise ValueError(
            "Missing or invalid numeric values found."
        )

    return X, y


# =========================================================
# Train-Test Split
# =========================================================

def split_data(X, y):

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    return X_train, X_test, y_train, y_test


# =========================================================
# Feature Scaling
# =========================================================

def scale_data(X_train, X_test):

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)

    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, scaler


# =========================================================
# Main
# =========================================================

if __name__ == "__main__":

    df = load_dataset()

    print("\nDataset information:")
    print(df.info())

    X, y = preprocess_data(df)

    print("\nFeatures:")
    print(FEATURES)

    print("\nClass distribution:")
    print(y.value_counts())

    X_train, X_test, y_train, y_test = split_data(X, y)

    X_train_scaled, X_test_scaled, scaler = scale_data(
        X_train,
        X_test
    )

    print("\nPreprocessing completed successfully.")

    print("Training samples:", len(X_train))
    print("Testing samples:", len(X_test))

    print("Training shape:", X_train_scaled.shape)
    print("Testing shape:", X_test_scaled.shape)
