def nansum(df, some_col: str, result: str = "nan_sum"):
    """
    Calculates the sum of elements in a column, ignoring empty values.
    :param some_col: The name of the column to calculate the sum over.
    :param result: Resulting column name
    """

    import numpy as np

    df[result] = np.nansum(df[some_col])

    return df
