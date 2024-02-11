def exp(df, some_col: str, result: str):
    """
    Returns e raised to the power of number. The constant e equals 2.71828182845904, the base of the natural logarithm.
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    import numpy as np
    df[result] = np.exp(df[some_col])

    return df
