from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

# Create Flask app
app = Flask(__name__)

# Load model and scaler (✅ use correct relative paths)
model = joblib.load('model/lightgbm_model.pkl')
scaler = joblib.load('model/scaler.pkl')

# Load feature names
feature_names = joblib.load('model/feature_columns.pkl')
feature_names_for_clustering = joblib.load('model/cluster_features.pkl')
kmeans = joblib.load('model/kmeans_model.pkl')

# Load utility functions
from utils.predict import prepare_input
from utils.recommendation_engine import generate_recommendations
from utils.shap_explainer import generate_shap_plots
from utils.cluster_recommendation import cluster_based_recommendation

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:

        form_data = dict(request.form)  # ✅ Convert to regular dict

        # Step 1: Feature engineering
        engineered, other_features = prepare_input(request.form)
        full_features = np.concatenate([engineered, other_features]).reshape(1, -1)

        # Step 2: Scaling
        scaled_input = scaler.transform(full_features)

        # Step 3: Create DataFrame for model
        input_df = pd.DataFrame(scaled_input, columns=feature_names)
        y_pred = model.predict(input_df)[0]

        # Step 4: SHAP plots (optional)
        generate_shap_plots(full_features)

        # Step 5: Prepare values for tips
        bmi = engineered[4]
        high_bp = int(engineered[2] > 130)
        high_chol = int(request.form['cholesterol']) > 1
        high_gluc = int(request.form['gluc']) > 1
        lifestyle_risk = other_features[-1]

        # Step 6: Calculate Age Gap
        try:
            actual_age = float(request.form.get('Chronological_Age', y_pred))
        except:
            actual_age = y_pred

        age_gap = y_pred - actual_age

        # Step 7: Get standard recommendations
        tips_obj = generate_recommendations(bmi, high_bp, high_chol, high_gluc, lifestyle_risk, age_gap)

        # Step 8: Cluster-based personalization
        map_val = engineered[3]  # Assuming MAP is at index 3
        cluster_input_df = pd.DataFrame(
            [[age_gap, bmi, map_val, lifestyle_risk]],
            columns=['Age_Gap', 'BMI', 'MAP', 'Lifestyle_Risk']
        )
        cluster_id = int(kmeans.predict(cluster_input_df)[0])
        cluster_tips, cluster_status = cluster_based_recommendation(cluster_id)

        # Step 9: Merge status and tips
        status = tips_obj.get('status', '') + " " + cluster_status

        # Step 10: Return to frontend
        return render_template(
        'result.html',
        predicted_age=round(y_pred, 1),
        tips=tips_obj['tips'] + cluster_tips,
        status=status,
        user_data=full_features.tolist()  # or just a safe string like form_data
    )



    except Exception as e:
        return f"\u274c Error during prediction: {str(e)}"


# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
