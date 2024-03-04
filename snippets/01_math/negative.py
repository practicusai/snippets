def negative(df, some_col: str, result: str):
    """
    Calculates the negative of elements in a column.
    :param some_col: The name of the column to calculate the negative values of.
    :param result: Resulting column name
    """

    import numpy as np

    df[result] = np.negative(df[some_col])

    return df
