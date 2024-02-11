def cos(df, some_col: str, result: str):
    """
    Returns the cosine of the given angle.
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    import numpy as np
    df[result] = np.cos(df[some_col])

    return df
