def is_even(df, some_numeric_col: str, result: str):
    """
    Determines whether values in a column are even or odd. 
    :param some_numeric_col: Name of the column to check for evenness. Must be a numeric type column.
    :param result: Name of the resulting column where the boolean values indicating evenness will be stored.
    """

    import numpy as np

    df[result] = np.where(df[some_numeric_col] % 2 == 0, True, False)
    return df
