def sign(df, numeric_col: str, result: str):
    """
    Determines the sign of values in a column.
    For each value in the specified column:
        - Returns 1 if the value is positive.
        - Returns 0 if the value is zero.
        - Returns -1 if the value is negative.
    
    :param numeric_col: Name of the column to calculate signs for.
    :param result: Name of the resulting column where the signs will be stored.
    """

    import numpy as np

    df[result] = np.sign(df[numeric_col])

    return df

