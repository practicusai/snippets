def tanh(df, some_col: str, result: str):
    """
    Tanh function is used to compute the hyperbolic tangent of the given angle of a column.
    :param some_col: Column containing angle values (in radians).
    :param result: Resulting column name
    """
    import numpy as np

    df[result] = np.tanh(df[some_col])

    return df
