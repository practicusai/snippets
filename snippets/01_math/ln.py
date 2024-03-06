def ln(df, numeric_col: str, result: str):
    """
    Calculates the natural logarithm of values in a column.
    :param numeric_col: Name of the column to apply the natural logarithm to.
                     Values in this column must be greater than 0.
    :param result: Name of the resulting column where the natural logarithm values will be stored.
    """

    import numpy as np

    # Check if all values in some_numeric_col are greater than 0
    if (df[numeric_col] <= 0).any():
        raise ValueError("Values in column '{}' must be greater than 0 for natural logarithm calculation.".format(numeric_col))

    df[result] = np.log(df[numeric_col])
    return df
