def absolute_value(df, some_col: str, result: str):
    """
    Returns the absolute value of a number. The absolute value of a number is the number without its sign.
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    import numpy as np

    df[result] = np.absolute(df[some_col])

    return df
