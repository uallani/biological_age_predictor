def cluster_based_recommendation(cluster_id):
    if cluster_id == 0:
        return [
            "🧪 You are biologically older than your actual age.",
            "🏃 Consider improving physical activity and getting regular health check-ups.",
            "🥗 Focus on reducing BMI through dietary changes."
        ], "You may be experiencing early aging signs."

    elif cluster_id == 1:
        return [
            "🎯 You are biologically younger than your actual age!",
            "💪 Great job! Just work on reducing excess weight to stay healthy long term.",
            "🍎 Maintain a balanced lifestyle — your aging is healthy."
        ], "You are aging better than your chronological age."

    elif cluster_id == 2:
        return [
            "⚠️ You may be at risk of metabolic conditions (high BMI, high BP).",
            "🩺 Consult a physician for hypertension and obesity management.",
            "🥦 Prioritize a low-sodium diet and stress reduction."
        ], "You are biologically at risk due to lifestyle and vitals."

    else:
        return ["❓ No specific recommendation available for this profile."], "Unknown cluster."
