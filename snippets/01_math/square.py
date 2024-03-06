def square(df, numeric_col: str, result: str):
    """
    Computes the element-wise square of values in a column.
    The square function calculates the square of each value in the specified column.

    :param numeric_col: The name of the column containing the values to calculate the square of.
    :param result: The name of the column where the resulting square values will be stored.
    """
    import numpy as np

    df[result] = np.square(df[numeric_col])

    return df
