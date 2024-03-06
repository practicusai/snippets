def log(df, some_numeric_col: str, base: int, result: str):
    """
    Calculates the logarithm of values in a column to the specified base.
    :param some_numeric_col: Name of the column to apply the logarithm to.
                     Values in this column must be greater than 0.
    :param base: The base of the logarithm. Must be an integer greater than 1.
    :param result: Name of the resulting column where the logarithm values will be stored.
    """
    import numpy as np

    # Check if all values in some_numeric_col are greater than 0
    if (df[some_numeric_col] <= 0).any():
        raise ValueError("Values in column '{}' must be greater than 0 for logarithm calculation.".format(some_numeric_col))

    # Check if base is greater than 1
    if base <= 1:
        raise ValueError("Base '{}' must be an integer greater than 1.".format(base))

    df[result] = np.log(df[some_numeric_col]) / np.log(base)  
    return df

