from enum import Enum


class NormalizationOptions(str, Enum):
    Z_SCORE = "Z-Score Normalization"
    MIN_MAX = "Min-Max Normalization"
    ROBUST = "Robust Normalization"

def normalize(df, some_numeric_col_list: list[str] | None, normalization_option: NormalizationOptions, result: list[str] | None):
    """
    Normalizes certain columns in the DataFrame with the selected normalization method.
    :param some_numeric_col: Names of the numeric columns to normalize
    :param normalization_option: Normalization method to use
    :param result_cols: Column names to write normalization results (Optional)
    :return: DataFrame with normalization applied
    """
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
    
    # If no specific columns provided, use all numeric columns
    if not some_numeric_col_list:
        some_numeric_col_list = df.select_dtypes(include=[np.number]).columns.tolist()

    # Process according to the selected normalization method
    if normalization_option == NormalizationOptions.Z_SCORE:
        scaler = StandardScaler()
    elif normalization_option == NormalizationOptions.MIN_MAX:
        scaler = MinMaxScaler()
    elif normalization_option == NormalizationOptions.ROBUST:
        scaler = RobustScaler()
    else:
        raise ValueError("Unsupported normalization option selected.")
    
    # Apply the normalization process and write the results in the corresponding columns
    for col, result_col in zip(some_numeric_col_list, result):
        df[result] = scaler.fit_transform(df[[col]])

    return df
