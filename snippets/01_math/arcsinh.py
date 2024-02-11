def arcsinh(df, some_col: str, result: str):
    """
    Inverse hyperbolic sine of the given angle, element-wise.
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    import numpy as np
    df[result] = np.arcsinh(df[some_col])

    return df
