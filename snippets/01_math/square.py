def square(df, some_col: str, result: str):
    """
    Square function is used to compute the element-wise square of a column.
    :param some_col: Column to calculate the square of
    :param result: Resulting column name
    """
    import numpy as np

    df[result] = np.square(df[some_col])

    return df
