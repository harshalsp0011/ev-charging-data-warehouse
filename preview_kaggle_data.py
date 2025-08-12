#!/usr/bin/env python3
"""
Preview Kaggle EV Charging Patterns Dataset
"""

import pandas as pd

def main():
    # Load the dataset
    df = pd.read_csv("data/external/ev_charging_patterns.csv")
    
    # Display basic information
    print("📈 Data Shape:", df.shape)
    print("\n📋 Columns and Data Types:")
    print(df.dtypes.to_string())
    
    print("\n🔎 Sample Rows:")
    print(df.head(10).to_string(index=False))
    
    print("\n🔍 Missing Values Summary:")
    print(df.isnull().sum().to_string())

if __name__ == "__main__":
    main()
