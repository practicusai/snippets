def cosh(df, some_col: str, result: str):
    """
    Returns the hyperbolic cosine of the given angle.
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    import numpy as np
    df[result] = np.cosh(df[some_col])

    return df

