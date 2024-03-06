def exp(df, numeric_col: str, result: str):
    """
    Calculates the exponential of the values in a specified column, and adds the result as a new column to the DataFrame.
    The constant e equals approximately 2.71828182845904, which is the base of the natural logarithm.
    :param numeric_col: Name of the column whose values are used for exponential calculation.
    :param result: Name of the resulting column where the exponential values will be stored.
    """
    import numpy as np
    df[result] = np.exp(df[numeric_col])

    return df
