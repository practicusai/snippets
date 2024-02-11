def log(df, some_col: str, base: int, result: str):
    """
    Calculates the logarithm of values in a column to the specified base.
    :param some_col: The name of the column to apply the logarithm to.
    :param base: The base of the logarithm
    :param result: Resulting column name
    """
    import numpy as np

    df[result] = np.log(df[some_col]) / np.log(base)  # Calculate log to any base
    return df
