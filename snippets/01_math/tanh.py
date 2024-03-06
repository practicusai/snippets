def tanh(df, some_numeric_col: str, result: str):
    """
    Calculates the hyperbolic tangent of angles in a column, assuming angles are given in radians.
    :param some_numeric_col: The name of the column containing the angle values in radians. 
    :param result: The name of the column where the resulting hyperbolic tangent values will be stored.
    """
    import numpy as np

    df[result] = np.tanh(df[some_numeric_col])

    return df
