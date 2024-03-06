def mod(df, some_numeric_col: str, divisor: int, result: str):
    """
    Calculates the remainder of division of values in a column by a divisor.
    :param some_numeric_col: Name of the column to apply the mod operation.
    :param divisor: Divisor to use for the mod operation.
                    Must be a non-zero integer.
    :param result: Name of the resulting column where the mod values will be stored.
    """

    import numpy as np

    # Check if divisor is non-zero
    if divisor == 0:
        raise ValueError("Divisor cannot be zero.")

    df[result] = np.mod(df[some_numeric_col], divisor)
    return df
