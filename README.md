# 🩺 Chronic Kidney Disease (CKD) Classification Using Machine Learning

This project is focused on building a **machine learning pipeline** to classify whether a person has Chronic Kidney Disease (CKD) based on medical test data. The final product is deployed as a **micro-site using Flask**, where users can input patient data and receive real-time predictions.

---

## 📁 Project Structure

```bash
.
├── app.py                       # Flask application
├── models/
│   ├── random_forest_model.pkl
│   └── naive_bayes_model.pkl
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   ├── predict.html
│   ├── result_good.html
│   └── result_bad.html
├── data/
│   └── chronickidneydisease.csv
├── requirements.txt
└── README.md
```

---

## 🧠 Objective

To accurately **classify CKD** and **support early diagnosis** by using various machine learning algorithms such as:

- Logistic Regression
- Naive Bayes
- Random Forest

The best-performing model is deployed in a user-friendly web interface using Flask.

---

## 📊 Dataset Overview

- **File**: `chronickidneydisease.csv`
- **Target variable**: `class` (1 - has CKD, 0 - no CKD)
- **Samples**: \~400 records
- **Features** (10 used in model):
  - `albumin` (numeric)
  - `sugar` (numeric)
  - `red_blood_cells` (categorical: yes=1, no=0)
  - `serum_creatinine` (numeric)
  - `hemoglobin` (numeric)
  - `red_blood_cell_count` (numeric)
  - `hypertension` (categorical: yes=1, no=0)
  - `diabetes_mellitus` (categorical: yes=1, no=0)
  - `appetite` (categorical: good=1, poor=0)
  - `pedal_edema` (categorical: yes=1, no=0)

---

## 🔍 Data Preprocessing

1. **Missing value handling**:

   - Used `SimpleImputer` with mean/most\_frequent strategies.

2. **Encoding categorical features**:

   - Label encoding (yes → 1, no → 0)

3. **Feature scaling**:

   - StandardScaler for numerical features.

4. **Outlier detection**:

   - Boxplots and z-scores were used.
   - No hard removal, treated with domain logic or left if clinically valid.

---

## 🎯 Feature Selection

Feature selection methods used:

- Correlation Matrix (visual)
- Recursive Feature Elimination (RFE)
- Domain knowledge

### Final selected features (10 total):

- Kept due to high correlation with CKD and clinical relevance.

---

## 🤖 Model Training

We trained and evaluated three models:

| Model               | Accuracy | F1 Score |
| ------------------- | -------- | -------- |
| Logistic Regression | \~96%    | High     |
| Naive Bayes         | \~97%    | High     |
| Random Forest       | \~98%    | Highest  |

### 📊 Evaluation Metrics:

- Accuracy
- Precision, Recall
- F1-Score
- Confusion Matrix
- Classification Report (printed for all)

Random Forest was selected for deployment due to its:

- Higher accuracy and F1 score
- Ability to handle non-linearity and feature interactions
- Robustness to noise and overfitting

---

## 🚀 Deployment with Flask

A micro-site was created using the **Flask framework** to allow easy input and prediction.

### HTML Pages:

1. **Home Page** (`index.html`)
2. **Prediction Page** (`predict.html`)
   - Takes numerical + dropdown inputs
3. **Result Pages**:
   - `result_good.html`: For patients not predicted to have CKD
   - `result_bad.html`: For those predicted with CKD

### Model Integration:

- Only Random Forest model (`random_forest_model.pkl`) is used for prediction
- Model was serialized using `pickle`

---

## 💻 Run the App Locally

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ckd-classification.git
cd ckd-classification
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate    # or venv\Scripts\activate on Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Flask app:

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 📅 Future Work

- Extend with other models like XGBoost or SVM.
- Add visualization of input and prediction confidence.
- Connect to a medical database or live API for hospital usage.

---

## 🙏 Acknowledgment

This project is part of a diploma in Artificial Intelligence and Machine Learning, focusing on applying ML in medical diagnosis. Special thanks to the mentors, peers, and the open-source community for support and tools.

---

## 📌 Tags

`Machine Learning` `Healthcare` `Classification` `Flask` `Chronic Kidney Disease` `Random Forest` `Naive Bayes` `Python` `Medical AI`

