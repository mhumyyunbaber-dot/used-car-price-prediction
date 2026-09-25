# 🚗 Used Car Price Prediction

> **An end-to-end machine learning regression project focused on predicting used-car prices and analyzing why models succeed or fail.**

## 🎯 Project Overview

Used-car pricing depends on many factors such as vehicle age, mileage, brand, model, engine characteristics, transmission, and vehicle condition.

The goal of this project was not simply to train a model, but to follow a realistic machine learning workflow:

**Problem → Data → Baseline → Model → Evaluation → Error Analysis → Feature Engineering → Model Comparison**

The project also demonstrates an important ML engineering principle: **when model performance is limited by the dataset, blindly tuning the model is not always the right solution.**

---

## 🧠 Problem Statement

A used-car business needs a way to estimate vehicle prices from available vehicle information.

Given a vehicle's characteristics, the system attempts to predict its price.

### Input Features

* Brand
* Model
* Model Year
* Mileage
* Engine Size
* Horsepower
* Fuel Type
* Transmission
* Exterior Color
* Interior Color
* Accident History
* Clean Title

### Target

**Vehicle Price**

Since price is a continuous numerical value, this is a **regression problem**.

---

## 🛠️ Tech Stack

* **Python**
* **Pandas** — data manipulation
* **NumPy** — numerical computation
* **Matplotlib** — data visualization
* **Scikit-learn** — preprocessing, modeling and evaluation
* **Jupyter Notebook** — experimentation and analysis
* **Git/GitHub** — version control

---

## 🔍 Data Preparation

The raw dataset was not directly ready for machine learning.

I performed the following preprocessing:

* Converted mileage strings such as `51,000 mi.` into numerical values.
* Converted prices such as `$38,005` into numerical values.
* Investigated missing values.
* Replaced missing categorical values with `Unknown`.
* Extracted **engine size** from unstructured engine descriptions.
* Extracted **horsepower** where available.
* Used median imputation for missing numerical engine features.
* Applied one-hot encoding to categorical variables.
* Used a train/test split to evaluate performance on unseen data.

---

## 📊 Modeling Approach

### 1. Baseline

The baseline predicted the average training-set price for every test vehicle.

| Metric | Result |
| ------ | -----: |
| MAE    | 35,276 |
| RMSE   | 35,276 |
| R²     | -0.002 |

This established a reference point before introducing machine learning models.

---

### 2. Linear Regression

The first machine learning model achieved:

| Metric |  Result |
| ------ | ------: |
| MAE    |  25,845 |
| RMSE   | 137,154 |
| R²     |   0.080 |

After extracting engine size and horsepower:

| Metric |  Result |
| ------ | ------: |
| MAE    |  25,353 |
| RMSE   | 135,565 |
| R²     |   0.101 |

This showed that the engineered engine features provided measurable improvement.

---

### 3. Random Forest Regression

A nonlinear model was then tested to capture relationships that Linear Regression could not represent effectively.

**Final result:**

| Metric |      Result |
| ------ | ----------: |
| MAE    |  **16,433** |
| RMSE   | **133,553** |
| R²     |   **0.127** |

Random Forest substantially reduced the average absolute prediction error compared with Linear Regression.

---

## 🔎 Error Analysis

Rather than removing unusual observations simply to improve the metrics, I investigated the largest prediction errors.

The extreme errors included vehicles such as:

* Bugatti Veyron
* Porsche Carrera GT
* Ford GT
* Dodge Viper
* Maserati Quattroporte

These were not obvious data-entry errors. They represented genuinely rare and extremely expensive vehicles.

The price distribution was also strongly right-skewed, with most vehicles concentrated at substantially lower prices and a small number of vehicles reaching several million dollars.

This explains why **RMSE remained very high despite the improvement in MAE**.

---

## 💡 What I Learned

This project reinforced several practical machine learning concepts:

### Baselines matter

A model should be compared against a simple baseline rather than judged in isolation.

### Feature engineering matters

Turning information hidden inside text into useful numerical features can improve model performance.

### Model choice matters

Random Forest captured nonlinear pricing relationships better than Linear Regression.

### Metrics tell different stories

MAE improved substantially, while RMSE remained high because of extreme prediction errors.

### More tuning is not always the answer

The experiments showed that the dataset itself was a significant limitation. Instead of endlessly tuning models to compensate for the data, the next iteration should use a more suitable dataset.

---

## ⚠️ Current Limitation

The final model achieved an R² of approximately **0.13**.

This is not strong enough to present the model as a production-ready vehicle pricing system.

Instead of hiding this limitation, the project documents **why the model struggled and what should be improved next**.

The next iteration will use a more consistent used-car dataset with better price distribution and feature coverage.

---

## 📁 Project Structure

```text
used-car-price-prediction/
│
├── data/
│   └── cars.csv
│
├── notebooks/
│   └── 01_data_analysis.ipynb
│
├── output.png
├── README.md
└── requirements.txt
```

> The dataset is excluded from version control through `.gitignore`.

---

## 🚀 Future Improvements

* Use a more suitable used-car dataset
* Improve feature engineering
* Compare additional tree-based models
* Analyze model errors by vehicle price range
* Build a simple prediction interface
* Deploy the final model as an API

---

## 👨‍💻 Project Focus

This project was built to demonstrate more than model training.

It focuses on:

**Problem Solving • Data Preparation • Feature Engineering • Model Selection • Evaluation • Error Analysis • Critical Thinking**

The main objective was to understand **why a model performs the way it does**, not simply achieve a high metric.

---

## 📌 Project Status

**Completed — ML experimentation and problem analysis phase**

The current version establishes the complete ML workflow and identifies the dataset as the primary limitation for further improvement.
