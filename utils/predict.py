# predict.py
import numpy as np

def prepare_input(form):
    """Extracts and engineers features from the form input."""
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

    # Feature engineering
    BMI = features[2] / ((features[1] / 100) ** 2)
    Pulse_Pressure = features[3] - features[4]
    MAP = (features[3] + 2 * features[4]) / 3
    SBP_DBP_Ratio = features[3] / features[4]
    HighChol_Flag = 1 if features[5] > 1 else 0
    HighGluc_Flag = 1 if features[6] > 1 else 0
    Lifestyle_Risk = 1 if features[7] + features[8] + (1 - features[9]) >= 2 else 0

    engineered = [features[1], features[2], features[3], features[4], BMI, MAP, Pulse_Pressure, SBP_DBP_Ratio]
    binary = [features[0], features[7], features[8], features[9], features[10], HighChol_Flag, HighGluc_Flag, Lifestyle_Risk]
    obesity_encoded = [4 if BMI >= 40 else 3 if BMI >= 30 else 2 if BMI >= 25 else 1]

    return np.array(engineered), binary + obesity_encoded

