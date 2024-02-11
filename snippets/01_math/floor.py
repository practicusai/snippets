def floor(df, some_col: str, significance: float, result: str):
    """
    Rounds values in a column down to the nearest multiple of significance.
    :param some_col: Column to calculate
    :param significance: The multiple to round to.
    :param result: Resulting column name
    """
    import numpy as np

    df[result] = np.floor(df[some_col] / significance) * significance
    return df
