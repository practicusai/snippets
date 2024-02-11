def sign(df, some_col: str, result: str):
    """
    Determines the sign of values in a column. Returns 1 for positive values, 0 for zero, and -1 for negative values.
    :param some_col: The name of the column to calculate signs for.
    :param result: Resulting column name
    """

    import numpy as np

    df[result] = np.sign(df[some_col])

    return df

