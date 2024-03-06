def remainder(df, first_numeric_col: str, second_numeric_col: str, result: str):
    """
    Calculates the element-wise remainder of division between two columns.
    :param first_numeric_col: Name of the first column containing the dividend.
    :param second_numeric_col: Name of the second column containing the divisor.
    :param result: Name of the resulting column where the remainders will be stored.
    """

    import numpy as np

    df[result] = np.remainder(df[first_numeric_col], df[second_numeric_col])

    return df
