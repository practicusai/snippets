def sin(df, numeric_col: str, result: str):
    """
    Calculates the sine of values in a column, assuming angles are in radians.
    :param numeric_col: Name of the column containing angles in radians.
    :param result: Name of the resulting column where the sine values will be stored.
    """

    import numpy as np

    df[result] = np.sin(df[numeric_col])

    return df

