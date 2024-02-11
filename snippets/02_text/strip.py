def strip(df, some_col: str, result: str):
    """
    Returns a copy with the leading and trailing characters removed
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    import numpy as np

    df[result] = np.char.strip(df[some_col])

    return df
