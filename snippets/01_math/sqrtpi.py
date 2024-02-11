def sqrtpi(df, some_col: str, result: str):
    """
    Sqrtpi function is used to compute the square root of (number * pi) for a column.
    :param some_col: Column to calculate the square root of (number * pi)
    :param result: Resulting column name
    """
    import numpy as np

    df[result] = np.sqrt(np.pi) * df[some_col]

    return df
