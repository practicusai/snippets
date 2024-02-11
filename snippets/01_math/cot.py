def cot(df, some_col: str, result: str):
    """
    Returns the cotangent of an angle specified in radians.
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    import numpy as np
    df[result] = 1 / np.tan(df[some_col])

    return df
