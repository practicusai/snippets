def suppress_outliers(
        df, outlier_col: list[str] | None, q1_percentile: float, q3_percentile: float,
        result_col_prefix: str | None, result_col_suffix: str | None):
    """
    Suppresses outliers in specified numeric columns of the dataframe based on custom percentile values for Q1 and Q3.
    Adds new columns with the selected prefix, or suffix. Only one of prefix or suffix can be used, not both.
    :param outlier_col: List of numeric columns to check for outliers. If left empty, applies to all numeric columns.
    :param q1_percentile: Custom percentile for Q1 (e.g., 0.20 for 20th percentile).
    :param q3_percentile: Custom percentile for Q3 (e.g., 0.80 for 80th percentile).
    :param result_col_prefix: Prefix for the result columns where the suppressed data will be stored.
    :param result_col_suffix: Or, suffix for the result columns where the suppressed data will be stored.
    """
    import numpy as np

    # If no specific columns provided, use all numeric columns
    if not outlier_col:
        outlier_col = df.select_dtypes(include=[np.number]).columns.tolist()

    if len(outlier_col) == 0:
        raise ValueError("No numeric column provided or located. ")

    # Process each specified column
    for col in outlier_col:
        q1 = df[col].quantile(q1_percentile)
        q3 = df[col].quantile(q3_percentile)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        if result_col_prefix:
            if result_col_suffix:
                raise ValueError("Either suffix or prefix should be provided, not both.")
            new_col_name = f'{result_col_prefix}_{col}'
        else:
            if not result_col_suffix:
                raise ValueError("One of suffix or prefix must be provided.")
            new_col_name = f'{col}_{result_col_suffix}'

        # Create a new column with suppressed values
        df[new_col_name] = np.where(
            df[col] < lower_bound, lower_bound, np.where(df[col] > upper_bound, upper_bound, df[col])
        )
    
    return df
