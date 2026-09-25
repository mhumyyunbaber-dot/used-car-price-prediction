# Used Car Price Prediction

A machine learning regression project that predicts used car prices from vehicle characteristics such as brand, model, year, mileage, engine information, fuel type, transmission, accident history, and title information.

## Problem

Used-car pricing depends on multiple factors, and estimating a reasonable price manually can be difficult.

The goal of this project was to build a regression model that could learn relationships between vehicle characteristics and their market price.

## Dataset

The project uses a public used-car price dataset containing approximately 4,000 vehicle records.

The dataset contains information such as:

* Brand
* Model
* Model year
* Mileage
* Fuel type
* Engine
* Transmission
* Exterior and interior color
* Accident history
* Clean title
* Price

## Data Preparation

The raw dataset required several preprocessing steps:

* Converted mileage from text such as `51,000 mi.` into numerical values.
* Converted price values such as `$38,005` into numerical values.
* Handled missing categorical values using an `Unknown` category.
* Extracted `engine_size` from engine descriptions.
* Extracted `horsepower` where available.
* Used median imputation for missing numerical engine features.
* Applied one-hot encoding to categorical features.

## Machine Learning Approach

The project followed this workflow:

1. Understand the real-world problem
2. Inspect the dataset
3. Clean the data
4. Separate features and target
5. Create a train/test split
6. Establish a baseline
7. Train Linear Regression
8. Analyze prediction errors
9. Engineer engine-related features
10. Train Random Forest Regression
11. Compare model performance
12. Analyze limitations

## Models and Results

### Baseline

The baseline predicted the average training-set price for every test vehicle.

* MAE: **35,276**
* RMSE: **35,276**
* R²: **-0.002**

### Linear Regression

* MAE: **25,845**
* RMSE: **137,154**
* R²: **0.080**

After adding engine size and horsepower:

* MAE: **25,353**
* RMSE: **135,565**
* R²: **0.101**

### Random Forest Regression

* MAE: **16,433**
* RMSE: **133,553**
* R²: **0.127**

Random Forest substantially reduced MAE compared with Linear Regression, showing that nonlinear models captured some pricing relationships better.

## Error Analysis

The largest prediction errors came from rare, extremely expensive vehicles such as:

* Bugatti Veyron
* Porsche Carrera GT
* Ford GT
* Dodge Viper
* Maserati Quattroporte

The dataset contains a strong right-skew in prices, with most vehicles concentrated in the lower price range while a small number of vehicles have prices reaching several million dollars.

This caused very large residuals and heavily affected RMSE.

## Key Learning

The project demonstrated that model performance is strongly influenced by the quality and characteristics of the dataset.

The experiments showed:

* A baseline is necessary for meaningful comparison.
* Linear Regression was too limited for the nonlinear pricing relationships in this dataset.
* Feature engineering improved Linear Regression slightly.
* Random Forest performed better, particularly in MAE.
* Extreme luxury vehicles created unusually large prediction errors.
* More complex modeling alone does not solve limitations caused by the underlying dataset.

## Current Limitation

The final Random Forest model achieved an R² of approximately **0.13**, which is not strong enough to consider this model a reliable production pricing system.

Rather than continuously tuning models to compensate for the dataset's limitations, the next iteration of this project will use a more suitable used-car dataset with more consistent pricing and feature coverage.

## Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Jupyter Notebook
* Git/GitHub

## Project Structure

```text
used-car-price-prediction/
│
├── data/
│   └── cars.csv
│
├── notebooks/
│   └── 01_data_analysis.ipynb
│
├── src/
│
├── README.md
└── requirements.txt
```

## Status

**Completed as an ML experimentation and problem-analysis project.**

The project intentionally stops before excessive model tuning because the dataset itself became the primary limitation. The next iteration will use a more suitable dataset and focus on building a stronger predictive system.
