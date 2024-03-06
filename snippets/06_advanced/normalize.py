from enum import Enum


class NormalizationOptions(str, Enum):
    Z_SCORE = "Z-Score Normalization"
    MIN_MAX = "Min-Max Normalization"
    ROBUST = "Robust Normalization"

def normalize(df, numeric_col_list: list[str] | None, normalization_option: NormalizationOptions, result: list[str] | None):
    """
    Normalizes certain columns in the DataFrame with the selected normalization method.
    :param numeric_col_list: Names of the numeric columns to normalize
    :param normalization_option: Specifies the method for normalization: Z-Score (standardizes data), Min-Max (scales data to a fixed range, typically [0, 1]), or Robust (reduces the impact of outliers).
    :param result_cols: Column names to write normalization results (Optional)
    :return: DataFrame with normalization applied
    """
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
    
    # If no specific columns provided, use all numeric columns
    if not numeric_col_list:
        numeric_col_list = df.select_dtypes(include=[np.number]).columns.tolist()

    # Process according to the selected normalization method
    if normalization_option == NormalizationOptions.Z_SCORE:
        scaler = StandardScaler()
    elif normalization_option == NormalizationOptions.MIN_MAX:
        scaler = MinMaxScaler()
    elif normalization_option == NormalizationOptions.ROBUST:
        scaler = RobustScaler()
    else:
        raise ValueError("Unsupported normalization option selected.")
    
    # Normalize specified columns and assign results either to new columns or overwrite them
    for i, col in enumerate(numeric_col_list):
        normalized_col_name = result[i] if result is not None and len(result) == len(numeric_col_list) else f"{col}_normalized"
        df[normalized_col_name] = scaler.fit_transform(df[[col]])

    return df
