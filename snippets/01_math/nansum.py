def nansum(df, numeric_col: str, result: str):
    """
    Calculates the sum of elements in a column, ignoring empty values.
    :param numeric_col: Name of the column to calculate the sum over.
    :param result: Name of the resulting column where the sum value will be stored.
    """

    import numpy as np

    df[result] = np.nansum(df[numeric_col])

    return df
