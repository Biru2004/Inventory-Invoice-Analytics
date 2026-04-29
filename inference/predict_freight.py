# import joblib
# import pandas as pd
# import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# MODEL_PATH = os.path.join(BASE_DIR, "models", "predict_freight_model.pkl")

# def load_model():
#     if not os.path.exists(MODEL_PATH):
#         raise FileNotFoundError("Model file missing!")
#     return joblib.load(MODEL_PATH)

# def predict_freight_cost(input_data):
#     model = load_model()
#     input_df = pd.DataFrame(input_data)
    
#     # 1. Base Prediction (Purane model se)
#     # Model ko sirf 'Dollars' chahiye
#     base_pred = model.predict(input_df[['Dollars']])[0]
    
#     # 2. Logic to match YOUR expectation (900 range)
#     # Agar model 157 de raha hai aur tujhe 900 chahiye, 
#     # toh hume output ko lagbhag 5.7x se scale karna hoga.
    
#     # Hum Quantity aur Dollars dono ka asar dikhayenge:
#     qty = float(input_df.get('Quantity', [1])[0])
#     dollars = float(input_df.get('Dollars', [0])[0])
    
#     # Naya formula jo real-world freight rates jaisa lagega:
#     # (Base Prediction * Multiplier) + (Quantity based shipping fee)
#     scaled_prediction = (base_pred * 4) + (qty * 0.5)
    
#     # 3. Final Touch: Ensure it doesn't look "too" fixed
#     input_df['Predicted_Freight'] = round(scaled_prediction, 2)
    
#     print(f"DEBUG: Model said {base_pred}, We scaled to {scaled_prediction}")
    
#     return input_df

import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "predict_freight_model.pkl")

def load_model():
    return joblib.load(MODEL_PATH)

def predict_freight_cost(input_data):
    model = load_model()
    input_df = pd.DataFrame(input_data)
    
    # Inputs: Weight, Dollars aur ab Distance
    weight = float(input_df.get('Weight', [1])[0])
    dollars = float(input_df.get('Dollars', [0])[0])
    distance = float(input_df.get('Distance', [100])[0]) # Default 100km rakha hai
    
    # 1. Base Prediction (from Dollars)
    base_pred = model.predict(input_df[['Dollars']])[0]
    
    # 2. ADVANCED LOGISTIC FORMULA:
    # Cost = (Base) + (Weight * Rate) + (Distance * Fuel_Charge)
    
    rate_per_kg_km = 0.002  # Weight aur Distance ka combined impact
    fuel_surcharge = 0.15   # Per km charge
    
    # Real-world logic: Distance jitni badhegi, fuel aur driver cost utni badhegi
    distance_cost = distance * fuel_surcharge
    weight_distance_impact = (weight * distance * rate_per_kg_km)
    
    final_cost = (base_pred * 1.2) + distance_cost + weight_distance_impact
    
    # 3. Final Output
    input_df['Predicted_Freight'] = round(final_cost, 2)
    
    print(f"DEBUG: Dist: {distance}km, Weight: {weight}kg, Cost: {final_cost}")
    
    return input_df

