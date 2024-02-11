def median(df, some_col: str, result: str):
    """
    Calculates the median of values in a column.
    :param some_col: The name of the column to apply the median to.
    :param result: Resulting column name
    """

    import numpy as np

    df[result] = np.median(df[some_col])
    return df
