def log2(df, some_col: str, result: str):
    """
    Calculates the base-2 logarithm of values in a column.
    :param some_col: The name of the column to apply the logarithm to.
    :param result: Resulting column name
    """

    import numpy as np

    df[result] = np.log2(df[some_col])
    return df
