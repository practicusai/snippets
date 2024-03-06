def log10(df, numeric_col: str, result: str):
    """
    Calculates the base-10 logarithm of values in a column.
    :param numeric_col: Name of the column to apply the base-10 logarithm to.
                            Values in this column must be greater than 0.
    :param result: Name of the resulting column where the base-10 logarithm values will be stored.
    """

    import numpy as np

    # Check if all values in numeric_col are greater than 0
    if (df[numeric_col] <= 0).any():
        raise ValueError("Values in column '{}' must be greater than 0 for logarithm calculation.".format(numeric_col))

    df[result] = np.log10(df[numeric_col])
    return df
