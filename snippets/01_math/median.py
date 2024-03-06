def median(df, some_numeric_col: str, result: str):
    """
    Calculates the median of values in a column.
    :param some_numeric_col: Name of the column to calculate the median.
                     Values in this column must be numeric.
    :param result: Name of the resulting column where the median value will be stored.
    """

    import numpy as np

    df[result] = np.median(df[some_numeric_col])
    return df
