def sumsq(df, some_numeric_col: str, result: str):
    """
    The sumsq function calculates the sum of the squares of each value in the specified column.
    :param some_numeric_col: The name of the column to calculate the sum of squares for.
    :param result: The name of the column where the resulting sum of squares will be stored.
    """
    import numpy as np

    df[result] = np.sum(np.square(df[some_numeric_col]))

    return df
