def arcsinh(df, numeric_col: str, result: str):
    """
    Calculates the inverse hyperbolic sine (arcsinh) of the values in a specified column, and adds the result as a new column to the DataFrame.
    :param numeric_col: Name of the column whose hyperbolic sine values are to be calculated.
    :param result: Name of the resulting column where the arcsinh values will be stored.
    """
    import numpy as np
    df[result] = np.arcsinh(df[numeric_col])

    return df
