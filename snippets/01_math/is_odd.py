def is_odd(df, some_col: str, result: str):
    """
    Determines whether values in a column are odd or even.
    :param some_col: The name of the column to check for oddness.
    :param result: Resulting column name
    """

    import numpy as np

    df[result] = np.where(df[some_col] % 2 != 0, True, False)  # Check for oddness
    return df
