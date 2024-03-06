def floor(df, numeric_col: str, significance: float, result: str):
    """
    Rounds values in a column down to the nearest multiple of significance.
    :param numeric_col: Name of the column containing the values to be rounded.
    :param significance: The multiple to round to. Values will be rounded down to the nearest multiple of this value. Must be a non-zero float.
    :param result: Name of the resulting column where the rounded values will be stored.
    """
    import numpy as np
    
    # Check if numeric_col exists and is numeric
    if numeric_col not in df.columns or not np.issubdtype(df[numeric_col].dtype, np.number):
        raise ValueError("Column '{}' does not exist or is not numeric.".format(numeric_col))
    
    # Check if significance is a non-zero float
    if not isinstance(significance, float) or significance == 0:
        raise ValueError("Significance must be a non-zero float.")

    df[result] = np.floor(df[numeric_col] / significance) * significance
    return df
