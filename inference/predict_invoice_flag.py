import pandas as pd

def load_model():
    # Model bypass (version mismatch ki wajah se)
    return None, None

def predict_invoice_flag(input_data):
    """
    Flexible prediction logic that handles different column names.
    """
    input_df = pd.DataFrame(input_data)
    
    # --- FLEXIBLE COLUMN PICKING ---
    # Agar 'Dollars' nahi mil raha, toh 'Invoice Dollars' ya 'Invoice_Dollars' check karega
    dollars = input_df.get('Dollars', 
              input_df.get('Invoice Dollars', 
              input_df.get('Invoice_Dollars', [0])))[0]
              
    quantity = input_df.get('Quantity', 
               input_df.get('Qty', [1]))[0] # Default quantity 1 rakha hai divide by zero se bachne ke liye

    # Logic: High price per unit or high total bill
    price_per_unit = float(dollars) / float(quantity) if float(quantity) > 0 else 0
    
    if price_per_unit > 500 or float(dollars) > 50000:
        prediction = 1  # Risky
    else:
        prediction = 0  # Normal
        
    input_df['Predicted_Flag'] = [prediction]
    
    print(f"DEBUG: Analyzed Dollars: {dollars}, Qty: {quantity}, Status: {prediction}")
    
    return input_df