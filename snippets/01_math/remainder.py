def remainder(df, first_col: str, second_col: str, result: str):
    """
    Calculates the element-wise remainder of division between two columns.
    :param first_col: The name of the first column containing the dividend.
    :param second_col: The name of the second column containing the divisor.
    :param result: Resulting column name
    """

    import numpy as np

    df[result] = np.remainder(df[first_col], df[second_col])

    return df
