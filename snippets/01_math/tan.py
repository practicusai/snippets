def tan(df, numeric_col: str, result: str):
    """
    Tan function is used to compute the tangent of the given angle of a column.
    :param numeric_col: The name of the column containing the angle values in radians.
    :param result: The name of the column where the resulting tangent values will be stored.
    """
    import numpy as np

    df[result] = np.tan(df[numeric_col])

    return df
