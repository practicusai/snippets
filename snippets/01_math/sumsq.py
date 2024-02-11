def sumsq(df, some_col: str, result: str):
    """
    Sumsq function is used to compute the sum of the squares of a column.
    :param some_col: Column to calculate the sum of the squares of
    :param result: Resulting column name
    """
    import numpy as np

    df[result] = np.sum(np.square(df[some_col]))

    return df
