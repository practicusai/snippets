def cbrt(df, some_col: str, result: str):
    """
    Return the cube-root of an array, element-wise.
    :param some_col: The cosine of the angle you want and must be from -1 to 1.
    :param result: Resulting column name
    """
    import numpy as np
    df[result] = np.cbrt(df[some_col])

    return df

