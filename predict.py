import joblib
import pandas as pd


# Load trained model
model = joblib.load("rf_car_price_model.pkl")


# Get car details from user
year = int(input("Enter car year: "))
engine_value = float(input("Enter engine size: "))
engine_unit = input("Enter engine unit (cc/kWh): ")
engine_type = input("Enter engine type (Petrol/Hybrid/Diesel): ")
transmission = input("Enter transmission (Automatic/Manual): ")
km_driven = int(input("Enter kilometers driven: "))
brand = input("Enter car brand: ")
model_name = input("Enter car model: ")


# Create input DataFrame
car = pd.DataFrame([{
    "year": year,
    "engine_value": engine_value,
    "engine_unit": engine_unit,
    "Engine_type": engine_type,
    "Transmission": transmission,
    "Km_Driven": km_driven,
    "brand": brand,
    "model_name": model_name
}])


# Predict price
prediction = model.predict(car)[0]


print("\nEstimated Car Price:")
print(f"{prediction:.2f} lakh PKR")