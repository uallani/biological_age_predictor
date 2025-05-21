# utils/predict.py

import numpy as np

def prepare_input(form):
    """
    Prepare features for LightGBM prediction.
    Returns two lists:
    - engineered: raw continuous features (height, weight, ap_hi, etc.)
    - other_features: binary + encoded features
    """
    try:
        features = [
            int(form['gender']),
            int(form['height']),
            float(form['weight']),
            int(form['ap_hi']),
            int(form['ap_lo']),
            int(form['cholesterol']),
            int(form['gluc']),
            int(form['smoke']),
            int(form['alco']),
            int(form['active']),
            int(form['cardio'])
        ]
    except KeyError as e:
        raise ValueError(f"Missing input: {e}")

    # Raw feature engineering
    BMI = features[2] / ((features[1] / 100) ** 2)
    MAP = (features[3] + 2 * features[4]) / 3
    Pulse_Pressure = features[3] - features[4]
    SBP_DBP_Ratio = features[3] / features[4]

    # Binary indicators
    HighChol_Flag = 1 if features[5] > 1 else 0
    HighGluc_Flag = 1 if features[6] > 1 else 0
    Lifestyle_Risk = 1 if features[7] + features[8] + (1 - features[9]) >= 2 else 0

    # Ordinal encoding for obesity
    if BMI >= 40:
        obesity_encoded = 4
    elif BMI >= 30:
        obesity_encoded = 3
    elif BMI >= 25:
        obesity_encoded = 2
    else:
        obesity_encoded = 1

    # Final feature list
    raw_features = [features[1], features[2], features[3], features[4], BMI, MAP, Pulse_Pressure, SBP_DBP_Ratio]
    binary = [features[0], features[7], features[8], features[9], features[10], HighChol_Flag, HighGluc_Flag, Lifestyle_Risk]

    return np.array(raw_features), binary + [obesity_encoded]
