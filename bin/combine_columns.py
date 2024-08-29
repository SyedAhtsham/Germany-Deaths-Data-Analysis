#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd

def combine_columns(df):
    """
    Combines corresponding age group columns in the DataFrame by summing their values.

    Returns:
    - df_combined: DataFrame with combined age group columns
    """
    
    # List of age group column names
    age_group_columns = [
        'under 1 year', '1 to under 15 years', '15 to under 20 years', '20 to under 25 years',
        '25 to under 30 years', '30 to under 35 years', '35 to under 40 years', '40 to under 45 years',
        '45 to under 50 years', '50 to under 55 years', '55 to under 60 years', '60 to under 65 years',
        '65 to under 70 years', '70 to under 75 years', '75 to under 80 years', '80 to under 85 years',
        '85 years and over', 'age unknown',
        'under 1 year.1', '1 to under 15 years.1', '15 to under 20 years.1', '20 to under 25 years.1',
        '25 to under 30 years.1', '30 to under 35 years.1', '35 to under 40 years.1', '40 to under 45 years.1',
        '45 to under 50 years.1', '50 to under 55 years.1', '55 to under 60 years.1', '60 to under 65 years.1',
        '65 to under 70 years.1', '70 to under 75 years.1', '75 to under 80 years.1', '80 to under 85 years.1',
        '85 years and over.1', 'age unknown.1'
    ]

    # Create a copy of the DataFrame to combine age group columns
    df_combined = df.copy(deep=True)

    # Iterate over pairs of columns, sum them up, and drop the duplicate columns
    for column in age_group_columns[:len(age_group_columns)//2]:  # Loop over half of the columns
        column_1 = column
        column_2 = column + ".1"
        df_combined[column] += df_combined[column_2]  # Add values of corresponding columns
        # Drop the corresponding .1 columns
        df_combined.drop(columns=column_2, inplace=True)

    # We can now use df_combined for further analysis, where age groups are combined

    return df_combined

