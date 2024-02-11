def apply_fix(df, some_col: str, result: str):
    """
    Fix function rounds elements of an array to the nearest integer toward zero.
    :param some_col: Column to apply fix operation
    :param result: Resulting column name
    """
    import numpy as np

    df[result] = np.fix(df[some_col])

    return df
