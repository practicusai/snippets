def sinh(df, some_numeric_col: str, result: str):
    """
    Calculates the hyperbolic sine of values in a column.
    :param some_numeric_col: Name of the column containing the values to calculate the hyperbolic sine of.
    :param result: Name of the column where the resulting hyperbolic sine values will be stored.
    """
    import numpy as np

    df[result] = np.sinh(df[some_numeric_col])

    return df
