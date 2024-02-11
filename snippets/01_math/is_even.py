def is_even(df, some_col: str, result: str):
    """
    Determines whether values in a column are even or odd.
    :param some_col: The name of the column to check for evenness.
    :param result: Resulting column name
    """

    import numpy as np

    df[result] = np.where(df[some_col] % 2 == 0, True, False)
    return df
