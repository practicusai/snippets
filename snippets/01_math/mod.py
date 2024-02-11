def mod(df, some_col: str, divisor: int, result: str):
    """
    Calculates the remainder of division of values in a column by a divisor.
    :param some_col: The name of the column to apply the mod to.
    :param divisor: The divisor to use.
    :param result: Resulting column name
    """

    import numpy as np

    df[result] = np.mod(df[some_col], divisor)
    return df
