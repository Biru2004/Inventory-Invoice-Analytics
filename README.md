📦 SigmaAI: Vendor Invoice Intelligence Portal
AI-Powered Freight Forecasting & Risk Analytics
🎯 Overview

SigmaAI is an advanced analytics dashboard designed for the modern logistics industry. It solves the complexity of freight budgeting and financial auditing by using Machine Learning to predict shipping costs and detect abnormal invoices before they impact the bottom line.

Built for the 2026 Logistics Landscape, it integrates real-world factors like fuel surcharges, weight-density ratios, and route distances.
✨ Key Features
🚚 1. Intelligent Freight Prediction

Unlike traditional static calculators, this engine uses a dynamic formula to estimate costs based on:

    Weight-to-Distance Correlation: Uses a Ton-Kilometer rate (0.002) to reflect actual truck wear and tear.

    Market-Adjusted Fuel Surcharges: Includes a 15% variable surcharge based on 2026 energy price standards.

    Invoice Value Weighting: Accounts for insurance and handling risks for high-value cargo.

🚨 2. Automated Risk Flagging

A dedicated ML module that scans vendor invoices to detect:

    Price Anomalies: Flags items with abnormal price-per-unit ratios.

    Financial Leakage: Detects inconsistencies between freight costs and item quantities.

    Approval Automation: Provides a "Safe" or "Manual Approval Required" status for finance teams.

🛠️ Tech Stack

    Frontend: Streamlit (Interactive Dashboard)

    Core Engine: Python 3.14

    Machine Learning: Scikit-Learn (Linear Regression & Decision Trees)

    Data Analytics: Pandas, NumPy

    Visualizations: Plotly Express

🚀 Installation & Setup

    Clone the Repository: ```bash

    git clone https://github.com/Biru2004/Inventory-Invoice-Analytics.git

    cd Inventory-Invoice-Analytics


    Install Dependencies: ```bash

    pip install -r requirements.txt


    Launch the Portal: ```bash

    streamlit run app.py


📊 Business Logic (2026 Standards)

The freight cost is calculated using a hybrid pricing model:

Cost=(Base_Model_Pred×1.2)+(Distance×Fuel_Surcharge)+(Weight×Distance×0.002)

This ensures that long-haul routes (like Kolkata to Delhi) reflect realistic operational expenses.
🤝 Acknowledgments

    Inspired by industry-standard logistics workflows.

    Core ML models optimized for high-dimensional invoice data.
