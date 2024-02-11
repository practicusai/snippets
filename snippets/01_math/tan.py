def tan(df, some_col: str, result: str):
    """
    Tan function is used to compute the tangent of the given angle of a column.
    :param some_col: Column containing angle values (in radians)
    :param result: Resulting column name
    """
    import numpy as np

    df[result] = np.tan(df[some_col])

    return df
