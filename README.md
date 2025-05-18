# 🧬 Biological Age Prediction using Cardiovascular Data

This project aims to estimate a person's **biological age** using health metrics collected during medical examinations. Biological age represents how old the body seems based on physiological conditions, as opposed to chronological age (actual age in years). By leveraging cardiovascular data and machine learning, we predict biological aging patterns and identify risk factors contributing to accelerated aging.

---

## 📁 Project Structure
biological_age_project/
├── data/
│ └── cardio_train.csv # Raw dataset
├── notebooks/
│ └── 01_EDA_and_Prep.ipynb # Main notebook for analysis and explanation
├── scripts/
│ ├── preprocessing.py # Data loading & feature engineering
│ └── model.py # Model training and evaluation
├── models/ # (Optional) Saved trained models
├── main.py # Pipeline entry point (optional)
└── README.md # Project overview

---

## 📊 Dataset Description

The dataset includes the following features:

### Objective Features
- `age` (in days) — will be converted to years
- `height` (in cm)
- `weight` (in kg)
- `gender` (1: women, 2: men)

### Examination Features
- `ap_hi` — systolic blood pressure
- `ap_lo` — diastolic blood pressure
- `cholesterol` (1: normal, 2: above normal, 3: well above normal)
- `gluc` (1: normal, 2: above normal, 3: well above normal)

### Subjective Features
- `smoke` (0: no, 1: yes)
- `alco` (alcohol intake)
- `active` (physical activity)

### Target (for reference)
- `cardio` — presence (1) or absence (0) of cardiovascular disease

---

## 🎯 Project Goal

1. **Convert** age in days to age in years (chronological age)
2. **Engineer** additional health features like BMI
3. **Train a regression model** to predict chronological age using health metrics
4. **Use predicted age** as an estimate of **biological age**
5. **Compute `age_gap`** = biological age − chronological age
6. **Visualize and explain** key factors behind biological aging using SHAP

---

## 🛠️ Tools & Libraries

- Python
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- SHAP
- Visual Studio Code
- Jupyter Notebook

---

## 📈 Expected Outcomes

- Well-structured, clean pipeline for predicting biological age
- EDA plots showing feature distributions and their correlation with aging
- Machine learning model performance: MAE, RMSE, R²
- SHAP visualizations to interpret important features
- Insights like: "High systolic BP and glucose levels are linked with older biological age"

---

## 🚀 How to Run the Project

1. Clone the repository or download the files
2. Open the project folder in **Visual Studio Code**
3. Install required packages using pip:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn shap
