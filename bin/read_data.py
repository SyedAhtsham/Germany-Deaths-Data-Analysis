# Import necessary libraries
import pandas as pd
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

def read_csv():
    """
    Read the CSV file containing Germany's deaths statistics and preprocess the data.
    
    Returns:
    - df: DataFrame containing overall death statistics
    - df_males: DataFrame containing death statistics for males
    - df_females: DataFrame containing death statistics for females
    """
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv("../data/Germany_Deaths.csv")
    
    # Set the index to 'Cause of Death' column
    df.set_index("Cause of Death", inplace=True)
    
    # Replace "-" and "." with 0
    df.replace(["-", "."], 0, inplace=True)
    
    # Convert columns (excluding 'Year') to numeric data type
    columns_to_convert = df.columns.difference(['Year'])
    df[columns_to_convert] = df[columns_to_convert].apply(pd.to_numeric, errors='ignore')
    
    # Separate columns for males and females
    df_males = df[[col for col in df.columns if ".1" not in col]]
    df_females = df[[col for col in df.columns if ".1" in col]]
    
    # Rename columns in the female DataFrame
    df_females.columns = [col.replace(".1", "") for col in df_females.columns]
    
    # Insert 'Year' column from df_males to df_females
    df_females.insert(loc=0, column='Year', value=df_males['Year'])
    
    return df, df_males, df_females
