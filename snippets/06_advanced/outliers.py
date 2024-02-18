def suppress_outliers_custom(df, columns: list[str] | None, q1_percentile: float, q3_percentile: float, result_col_prefix: str):
    import pandas as pd
    import numpy as np
    """
    Suppresses outliers in specified numeric columns of the dataframe based on custom percentile values for Q1 and Q3.
    :param df: DataFrame to process.
    :param columns: List of numeric columns to check for outliers. If None, applies to all numeric columns.
    :param q1_percentile: Custom percentile for Q1 (e.g., 0.20 for 20th percentile).
    :param q3_percentile: Custom percentile for Q3 (e.g., 0.80 for 80th percentile).
    :param result_col_prefix: Prefix for the result columns where the suppressed data will be stored.
    """
    # If no specific columns provided, use all numeric columns
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns.tolist()

    # Process each specified column
    for col in columns:
        Q1 = df[col].quantile(q1_percentile)
        Q3 = df[col].quantile(q3_percentile)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Create a new column with suppressed values
        df[f'{result_col_prefix}_{col}'] = np.where(df[col] < lower_bound, lower_bound,
                                                    np.where(df[col] > upper_bound, upper_bound, df[col]))
    
    return df
