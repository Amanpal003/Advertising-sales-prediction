Advertising Sales Prediction 📊

Project Overview

The objective of this project is to predict sales based on advertising budgets spent on TV, Radio, and Newspaper using Multiple Linear Regression.

A user can enter advertising budgets through a Streamlit web application and get predicted sales.

Project Structure

Advertising-Sales-Prediction/
│
├── data/
│   └── advertising_data.csv
│
├── frontend/
│   └── app.py
│
├── models/
│   └── linear_regression_model.pkl
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   └── 02_Model_Training.ipynb
│
├── src/
│   └── generate_data.py
│
├── .gitignore
└── README.md

Dataset Information

- Total Records: 100
- Total Columns: 4
- Input Features: TV, Radio, Newspaper
- Target Variable: Sales

Note: The dataset is synthetically generated for educational purposes.

Machine Learning Algorithm

Multiple Linear Regression

Used to predict Sales using three independent variables: TV, Radio, and Newspaper.

Technologies Used

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

Project Workflow

1. Dataset Generation
2. Data Loading and EDA
3. Data Visualization
4. Correlation Analysis
5. Train-Test Split
6. Model Training
7. Sales Prediction
8. Model Evaluation
9. Model Saving using Joblib
10. Streamlit Web Application

Model Evaluation

- MAE
- MSE
- RMSE
- R² Score
- Actual vs Predicted Graph

Run Locally

git clone https://github.com/Amanpal003/Advertising-sales-prediction.git


cd Advertising-Sales-Prediction
pip install pandas numpy matplotlib seaborn scikit-learn joblib streamlit
python -m streamlit run frontend/app.py

Application Features

- Enter TV, Radio and Newspaper budgets.
- Predict Sales instantly.
- View total advertising budget.
- View model evaluation metrics and graph.

Author

AMAN PAL
