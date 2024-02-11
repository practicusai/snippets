def sqrt(df, some_col: str, result: str):
    """
    Sqrt function is used to compute the square root of a column.
    :param some_col: Column to calculate the square root of
    :param result: Resulting column name
    """
    import numpy as np

    df[result] = np.sqrt(df[some_col])

    return df
