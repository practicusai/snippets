def trunc(df, some_numeric_col: str, result: str):
    """
    This function truncates the numbers in the specified column to integers by removing their fractional parts. 
    For example, 3.14 becomes 3, -4.9 becomes -4, and so on.
    :param some_numeric_col: The name of the column containing the numbers to truncate.
    :param result: Resulting column name to store the truncated values.
    """
    import numpy as np

    df[result] = np.trunc(df[some_numeric_col])

    return df
