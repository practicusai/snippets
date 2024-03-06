def negative(df, numeric_col: str, result: str):
    """
    Calculates the negative of elements in a column.
    :param numeric_col: Name of the column to calculate the negative values of.
    :param result: Name of the resulting column where the negative values will be stored.
    """

    import numpy as np

    df[result] = np.negative(df[numeric_col])

    return df
