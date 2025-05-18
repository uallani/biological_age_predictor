# utils/age_gap_recommendation.py

def generate_age_gap_tips(age_gap):
    """
    Generate a general status message based on the age gap.
    Positive age_gap = biological age > actual age (aging faster).
    Negative age_gap = biological age < actual age (aging slower).
    """
    if age_gap > 5:
        return "⚠️ You're aging faster than your actual age.", "Consider reviewing your health habits."
    elif age_gap < -5:
        return "🎉 You're aging slower than your actual age.", "Keep up the good work!"
    else:
        return "✅ You are aging in line with your actual age.", "Maintain your current lifestyle."
