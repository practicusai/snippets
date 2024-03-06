def gcd(df, first_integer_col: str, second_integer_col: str, result: str):
    """
    Calculates the greatest common divisor of values in two columns.
    :param first_integer_col: Name of the first column containing the values. Must be an integer type column.
    :param second_integer_col: Name of the second column containing the values. Must be an integer type column.
    :param result: Name of the resulting column where the greatest common divisor values will be stored.
    """

    import numpy as np

    df[result] = np.gcd(df[first_integer_col], df[second_integer_col])
    return df
