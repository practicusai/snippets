def acot(df, some_col: str, result: str):
    """
    Returns the principal value of the arccotangent, or inverse cotangent, of a number.
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    import numpy as np

    df[result] = np.pi/2 - np.arctan(df[some_col])

    return df
