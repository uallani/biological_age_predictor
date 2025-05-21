from .age_gap_recommendation import generate_age_gap_tips

def generate_recommendations(bmi, high_bp, high_chol, high_gluc, lifestyle_risk, age_gap=None):
    tips = []

    # Base health recommendations
    if bmi >= 30:
        tips.append(" You may be obese. Consider consulting a doctor about weight management.")
    if high_bp:
        tips.append(" Your blood pressure is high. Consider regular monitoring and reducing sodium.")
    if high_chol:
        tips.append(" Your cholesterol level is high. Consider a heart-healthy diet.")
    if high_gluc:
        tips.append(" Elevated glucose. Monitor for pre-diabetes/diabetes.")
    if lifestyle_risk:
        tips.append(" Improve your lifestyle: Exercise regularly and eat healthier.")

    # Age gap insight (if provided)
    if age_gap is not None:
        _, age_tip = generate_age_gap_tips(age_gap)
        tips.append(age_tip)

    return {"tips": tips}
