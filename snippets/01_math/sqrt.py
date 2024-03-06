def sqrt(df, numeric_col: str, result: str):
    """
    Calculates the square root of values in a column.
    :param numeric_col: Name of the column containing the values to calculate the square root of.
    :param result: Name of the column where the resulting square root values will be stored.
    """
    import numpy as np

    df[result] = np.sqrt(df[numeric_col])

    return df
