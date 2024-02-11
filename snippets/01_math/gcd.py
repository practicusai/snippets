def gcd(df, some_col1: str, some_col2: str, result: str):
    """
    Calculates the greatest common divisor of values in two columns.
    :param some_col1: The name of the first column.
    :param some_col2: The name of the second column.
    :param result: Resulting column name
    """

    import numpy as np

    df[result] = np.gcd(df[some_col1], df[some_col2])
    return df
