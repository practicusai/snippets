def sin(df, some_col: str, result: str):
    """
    Calculates the sine of values in a column, assuming angles are in radians.
    :param some_col: The name of the column containing angles in radians.
    :param result: Resulting column name
    """

    import numpy as np

    df[result] = np.sin(df[some_col])

    return df
