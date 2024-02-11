def sinh(df, some_col: str, result: str):
    """
    Calculates the hyperbolic sine of values in a column.
    :param some_col: The name of the column containing the values to calculate the hyperbolic sine of.
    :param result: Resulting column name
    """
    import numpy as np

    df[result] = np.sinh(df[some_col])

    return df
