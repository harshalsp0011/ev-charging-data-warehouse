#!/usr/bin/env python3
"""
Kaggle EV Dataset Analysis for Data Warehouse Schema Design
Performs data quality checks, explores structure, and suggests schema design.
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os


def load_and_inspect_data():
    """Load the Kaggle EV dataset and perform basic inspection"""
    
    print("Loading Kaggle EV Charging Dataset")
    print("=" * 60)
    
    try:
        # Load dataset from external folder
        df = pd.read_csv("data/external/ev_charging_patterns.csv")
        
        # Print general dataset info
        print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
        print(f"Memory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        
        return df
        
    except FileNotFoundError:
        print("File not found: data/external/ev_charging_patterns.csv")
        return None


def analyze_data_quality(df):
    """Check dataset quality: missing values, data types, duplicates, keys"""
    
    print("\nData Quality Analysis")
    print("-" * 40)
    
    # Missing values by column
    missing_data = df.isnull().sum()
    missing_percent = (missing_data / len(df)) * 100
    print("Missing Values by Column:")
    for col, missing, percent in zip(df.columns, missing_data, missing_percent):
        print(f"  {col:<30}: {missing:>4} ({percent:>5.1f}%)")
    
    # Data types of columns
    print("\nData Types:")
    for col, dtype in df.dtypes.items():
        print(f"  {col:<30}: {dtype}")
    
    # Count duplicate rows
    duplicates = df.duplicated().sum()
    print(f"\nDuplicate Rows: {duplicates}")
    
    # Check composite key uniqueness (User ID + Charging Start Time)
    composite_key_duplicates = df.duplicated(subset=['User ID', 'Charging Start Time']).sum()
    print(f"Duplicate User+StartTime combinations: {composite_key_duplicates}")
    
    return missing_data, missing_percent


def analyze_key_fields(df):
    """Check uniqueness and value distributions of important key fields"""
    
    print("\nKey Field Analysis")
    print("-" * 40)
    
    key_fields = [
        'User ID', 'Charging Station ID', 'Vehicle Model',
        'Charging Station Location', 'Charger Type', 'User Type'
    ]
    
    for field in key_fields:
        if field in df.columns:
            unique_count = df[field].nunique()
            total_count = len(df)
            print(f"{field:<30}: {unique_count} unique values ({unique_count/total_count*100:.1f}%)")
            
            # Show top 5 most common values
            top_values = df[field].value_counts().head(5)
            print(f"    Top values: {', '.join([f'{v}({c})' for v, c in zip(top_values.index, top_values.values)])}")
        else:
            print(f"{field:<30}: Field not found")


def analyze_numeric_fields(df):
    """Analyze numeric fields for stats, outliers, and validity"""
    
    print("\nNumeric Field Analysis")
    print("-" * 40)
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    for col in numeric_cols:
        print(f"\n{col}:")
        print(f"  Count:   {df[col].count():>8}")
        print(f"  Min:     {df[col].min():>10.2f}")
        print(f"  Max:     {df[col].max():>10.2f}")
        print(f"  Mean:    {df[col].mean():>10.2f}")
        print(f"  Median:  {df[col].median():>10.2f}")
        print(f"  Std Dev: {df[col].std():>10.2f}")
        
        # Check for outliers (beyond ±3 standard deviations)
        mean = df[col].mean()
        std = df[col].std()
        outliers = df[(df[col] < mean - 3*std) | (df[col] > mean + 3*std)][col].count()
        if outliers > 0:
            print(f"  Outliers (±3σ): {outliers}")
        
        # Validate no invalid negative/zero values for selected columns
        if col in ['Energy Consumed (kWh)', 'Charging Duration (hours)', 
                   'Charging Rate (kW)', 'Charging Cost (USD)', 'Battery Capacity (kWh)']:
            negative_count = (df[col] < 0).sum()
            zero_count = (df[col] == 0).sum()
            if negative_count > 0:
                print(f"  Negative values: {negative_count}")
            if zero_count > 0:
                print(f"  Zero values: {zero_count}")


def analyze_datetime_fields(df):
    """Validate and analyze datetime columns"""
    
    print("\nDateTime Field Analysis")
    print("-" * 40)
    
    datetime_fields = ['Charging Start Time', 'Charging End Time']
    
    for field in datetime_fields:
        if field in df.columns:
            print(f"\n{field}:")
            try:
                dt_series = pd.to_datetime(df[field])
                print(f"  Valid datetime format")
                print(f"  Date range: {dt_series.min()} to {dt_series.max()}")
                
                # Identify future timestamps
                future_dates = dt_series > datetime.now()
                if future_dates.any():
                    print(f"  Future dates: {future_dates.sum()}")
                    
            except Exception as e:
                print(f"  Parsing error: {str(e)}")
                print(f"  Sample values: {df[field].head(3).tolist()}")


def map_to_star_schema(df):
    """Suggest fact and dimension table mapping for star schema"""
    
    print("\nStar Schema Mapping")
    print("-" * 40)
    
    # Fact table
    fact_fields = [
        'User ID', 'Charging Station ID', 'Charging Start Time', 
        'Energy Consumed (kWh)', 'Charging Duration (hours)',
        'Charging Rate (kW)', 'Charging Cost (USD)',
        'Distance Driven (since last charge) (km)',
        'State of Charge (Start %)', 'State of Charge (End %)'
    ]
    print("FACT_CHARGING_SESSIONS:")
    for field in fact_fields:
        if field in df.columns:
            print(f"   {field}")
        else:
            print(f"   {field} (missing)")
    
    # Dimension tables
    dimensions = {
        'DIM_VEHICLE': ['Vehicle Model', 'Battery Capacity (kWh)', 'Vehicle Age (years)'],
        'DIM_STATION': ['Charging Station ID', 'Charging Station Location', 'Charger Type'],
        'DIM_USER': ['User ID', 'User Type'],
        'DIM_TIME': ['Charging Start Time', 'Time of Day', 'Day of Week'],
        'DIM_WEATHER': ['Temperature (°C)']
    }
    
    for dim_name, dim_fields in dimensions.items():
        print(f"\n{dim_name}:")
        for field in dim_fields:
            if field in df.columns:
                print(f"  {field}")
            else:
                print(f"  {field} (missing)")


def identify_data_cleaning_needs(df):
    """Identify required cleaning tasks for the dataset"""
    
    print("\nData Cleaning Requirements")
    print("-" * 40)
    
    cleaning_tasks = []
    
    # Validate timestamp format
    timestamp_fields = ['Charging Start Time', 'Charging End Time']
    for field in timestamp_fields:
        if field in df.columns:
            try:
                pd.to_datetime(df[field])
                print(f"{field}: Valid datetime format")
            except:
                print(f"{field}: Requires datetime conversion")
                cleaning_tasks.append(f"Convert {field} to datetime")
    
    # Check missing values in critical columns
    critical_fields = ['User ID', 'Charging Station ID', 'Energy Consumed (kWh)', 'Charging Duration (hours)']
    for field in critical_fields:
        if field in df.columns:
            missing_count = df[field].isnull().sum()
            if missing_count > 0:
                print(f"{field}: {missing_count} missing values")
                cleaning_tasks.append(f"Handle missing values in {field}")
            else:
                print(f"{field}: No missing values")
    
    # Validate zero/negative values in key metrics
    metric_fields = ['Energy Consumed (kWh)', 'Charging Duration (hours)', 'Charging Cost (USD)']
    for field in metric_fields:
        if field in df.columns:
            zero_count = (df[field] == 0).sum()
            negative_count = (df[field] < 0).sum()
            if zero_count > 0:
                print(f"{field}: {zero_count} zero values")
                cleaning_tasks.append(f"Validate zero values in {field}")
            if negative_count > 0:
                print(f"{field}: {negative_count} negative values")
                cleaning_tasks.append(f"Fix negative values in {field}")
    
    print(f"\nSummary: {len(cleaning_tasks)} cleaning tasks identified")
    return cleaning_tasks


def generate_schema_recommendations(df):
    """Generate sample Snowflake schema DDL recommendations"""
    
    print("\nSnowflake Schema Recommendations")
    print("-" * 40)
    
    print("CREATE SCHEMA DDL Recommendations:")
    print("\n-- FACT TABLE")
    print("CREATE OR REPLACE TABLE ANALYTICS.FACT_CHARGING_SESSIONS (")
    print("    session_id STRING PRIMARY KEY,")
    print("    user_id INTEGER,")
    print("    station_id STRING,")
    print("    date_id INTEGER,")
    print("    start_timestamp TIMESTAMP_LTZ,")
    print("    end_timestamp TIMESTAMP_LTZ,")
    print("    energy_consumed_kwh FLOAT,")
    print("    duration_hours FLOAT,")
    print("    charging_rate_kw FLOAT,")
    print("    charging_cost_usd FLOAT,")
    print("    distance_driven_km FLOAT,")
    print("    start_soc_percent INTEGER,")
    print("    end_soc_percent INTEGER")
    print(");")
    
    print("\n-- DIMENSION TABLES")
    print("CREATE OR REPLACE TABLE ANALYTICS.DIM_USER (")
    print("    user_id INTEGER PRIMARY KEY,")
    print("    user_type STRING")
    print(");")
    
    print("\nCREATE OR REPLACE TABLE ANALYTICS.DIM_STATION (")
    print("    station_id STRING PRIMARY KEY,")
    print("    station_location STRING,")
    print("    charger_type STRING")
    print(");")


def save_analysis_results(df, cleaning_tasks):
    """Save analysis reports into reports/ directory"""
    
    print("\nSaving Analysis Results")
    print("-" * 40)
    
    # Create reports directory if required
    os.makedirs("reports", exist_ok=True)
    
    # Metadata + cleaning report
    with open("reports/data_quality_report.txt", "w") as f:
        f.write("EV Charging Dataset - Data Quality Report\n")
        f.write("="*50 + "\n")
        f.write(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns\n")
        f.write(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("Columns and Data Types:\n")
        for col, dtype in df.dtypes.items():
            f.write(f"- {col}: {dtype}\n")
        
        f.write("\nMissing Values:\n")
        missing_data = df.isnull().sum()
        for col, missing in missing_data.items():
            if missing > 0:
                f.write(f"- {col}: {missing} missing values\n")
        
        f.write("\nData Cleaning Tasks:\n")
        for task in cleaning_tasks:
            f.write(f"- {task}\n")
    
    # Detailed numeric and sample reports
    df.describe().to_csv("reports/numeric_summary.csv")
    df.head(20).to_csv("reports/sample_data.csv", index=False)
    
    print("Saved analysis reports:")
    print("  reports/data_quality_report.txt")
    print("  reports/numeric_summary.csv")
    print("  reports/sample_data.csv")


def main():
    """Execute full analysis workflow"""
    
    print("EV Charging Dataset Analysis")
    print("=" * 60)
    print(f"Analysis Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Load dataset
    df = load_and_inspect_data()
    if df is None:
        return
    
    # Run analysis modules
    missing_data, missing_percent = analyze_data_quality(df)
    analyze_key_fields(df)
    analyze_numeric_fields(df)
    analyze_datetime_fields(df)
    map_to_star_schema(df)
    cleaning_tasks = identify_data_cleaning_needs(df)
    generate_schema_recommendations(df)
    
    # Save outputs
    save_analysis_results(df, cleaning_tasks)
    
    print("\nData Analysis Complete!")
    print("Ready for star schema implementation in Snowflake")
    print("Ready for ETL pipeline development")


if __name__ == "__main__":
    main()
