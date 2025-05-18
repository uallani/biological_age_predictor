# shap_explainer.py
import shap
import matplotlib.pyplot as plt
import joblib
import numpy as np

# Load model and scaler
model = joblib.load('model/lightgbm_model.pkl')
scaler = joblib.load('model/scaler.pkl')

def generate_shap_plots(X_input, instance_index=0):
    """Generates SHAP bar and waterfall plots for global and local explanations."""
    X_scaled = scaler.transform(X_input)
    explainer = shap.Explainer(model, X_scaled)
    shap_values = explainer(X_scaled)

    # Global importance
    shap.plots.bar(shap_values, show=False)
    plt.title("Global SHAP Feature Importance")
    plt.tight_layout()
    plt.savefig("static/shap_global_bar.png", dpi=300)
    plt.close()

    # Local explanation for one instance
    shap.plots.waterfall(shap_values[instance_index], show=False)
    plt.title("Local SHAP Waterfall Plot")
    plt.tight_layout()
    plt.savefig("static/shap_local_waterfall.png", dpi=300)
    plt.close()
