def cbrt(df, some_numeric_col: str, result: str):
    """
    Calculates the cube root of the values in a specified column.
    :param some_numeric_col: Name of the column whose values are to be calculated.
    :param result: Name of the resulting column where the cube root values will be stored.
    """
    import numpy as np

    df[result] = np.cbrt(df[some_numeric_col])

    return df
