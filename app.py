from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load model and metadata
model = joblib.load('model/lightgbm_model.pkl')
feature_names = joblib.load('model/feature_columns.pkl')
cluster_features = joblib.load('model/cluster_features.pkl')
kmeans = joblib.load('model/kmeans_model.pkl')

# Load utility functions
from utils.predict import prepare_input
from utils.recommendation_engine import generate_recommendations
from utils.cluster_recommendation import cluster_based_recommendation

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        form_data = dict(request.form)

        # Step 1: Extract features from form
        engineered, other_features = prepare_input(form_data)
        full_features = np.concatenate([engineered, other_features]).reshape(1, -1)

        # Step 2: Predict biological age
        input_df = pd.DataFrame(full_features, columns=feature_names)
        y_pred = model.predict(input_df)[0]

        # Step 3: Parse values for logic
        bmi = engineered[4]
        map_val = engineered[5]
        high_bp = int(engineered[2] > 130)
        high_chol = int(form_data['cholesterol']) > 1
        high_gluc = int(form_data['gluc']) > 1
        lifestyle_risk = other_features[-1]

        # Step 4: Age gap
        try:
            actual_age = float(form_data.get('Chronological_Age', y_pred))
        except:
            actual_age = y_pred
        age_gap = y_pred - actual_age

        # Step 5: General health tips
        tips_obj = generate_recommendations(bmi, high_bp, high_chol, high_gluc, lifestyle_risk, age_gap)

        # Step 6: Cluster-based suggestions
        cluster_input_df = pd.DataFrame([[age_gap, bmi, map_val, lifestyle_risk]], columns=cluster_features)
        cluster_id = int(kmeans.predict(cluster_input_df)[0])
        cluster_tips, _ = cluster_based_recommendation(cluster_id)

        # Step 7: Final output
        return render_template(
            'result.html',
            predicted_age=round(y_pred, 1),
            tips=tips_obj['tips'] + cluster_tips,
            user_data=form_data
        )

    except Exception as e:
        return f"❌ Error during prediction: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
