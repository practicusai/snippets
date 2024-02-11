def trunc(df, some_col: str, result: str):
    """
    Trunc function is used to truncate numbers in a column to integers by removing their fractional parts.
    :param some_col: Column containing numbers to truncate.
    :param result: Resulting column name
    """
    import numpy as np

    df[result] = np.trunc(df[some_col])

    return df
