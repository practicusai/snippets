def is_odd(df, some_numeric_col: str, result: str):
    """
    Determines whether values in a column are odd or even.
    :param some_numeric_col: Name of the column to check for oddness. Must be a numeric type column.
    :param result: Name of the resulting column where the boolean values indicating oddness will be stored.
    """

    import numpy as np

    df[result] = np.where(df[some_numeric_col] % 2 != 0, True, False)  # Check for oddness
    return df
