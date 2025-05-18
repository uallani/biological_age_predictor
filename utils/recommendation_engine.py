from .age_gap_recommendation import generate_age_gap_tips

def generate_recommendations(bmi, high_bp, high_chol, high_gluc, lifestyle_risk, age_gap=None):
    tips = []
    
    # Base recommendations
    if bmi >= 30:
        tips.append("⚖️ You may be obese. Consider consulting a doctor about weight management.")
    if high_bp:
        tips.append("💓 Your blood pressure is high. Consider regular monitoring and reducing sodium.")
    if high_chol:
        tips.append("🥚 Your cholesterol level is high. Consider a heart-healthy diet.")
    if high_gluc:
        tips.append("🍬 Elevated glucose. Monitor for pre-diabetes/diabetes.")
    if lifestyle_risk:
        tips.append("🚶 Improve your lifestyle: Exercise regularly and eat healthier.")

    # Age Gap logic
    status = "Matched"
    if age_gap is not None:
        if age_gap > 0:
            tips.append("🔴 You're biologically older than your actual age. Focus on sleep, stress, and healthy habits.")
            status = "Biologically Older"
        elif age_gap < 0:
            tips.append("🟢 You're biologically younger! Keep up the great work.")
            status = "Biologically Younger"
        else:
            tips.append("🟡 Your biological and chronological ages match well.")
            status = "Matched"

    return {"tips": tips, "status": status}
