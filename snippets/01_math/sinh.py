def sinh(df, numeric_col: str, result: str):
    """
    Calculates the hyperbolic sine of values in a column.
    :param numeric_col: Name of the column containing the values to calculate the hyperbolic sine of.
    :param result: Name of the column where the resulting hyperbolic sine values will be stored.
    """
    import numpy as np

    df[result] = np.sinh(df[numeric_col])

    return df
