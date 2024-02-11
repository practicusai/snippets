def log10(df, some_col: str, result: str = "log10_values"):
    """
    Calculates the base-10 logarithm of values in a column.
    :param some_col: The name of the column to apply the logarithm to.
    :param result: Resulting column name
    """

    import numpy as np

    df[result] = np.log10(df[some_col])
    return df
