def ln(df, some_col: str, result: str):
    """
    Calculates the natural logarithm of values in a column.

    :param some_col: The name of the column to apply the natural logarithm to.
    :param result: Resulting column name
    """

    import numpy as np
    df[result] = np.log(df[some_col])
    return df
