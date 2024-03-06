def arccos(df, numeric_col: str, result: str):
    """
    Trigonometric inverse cosine, element-wise. The inverse of cos so that, if y = cos(x), then x = arccos(y).

    :param numeric_col: Required. Name of the column whose cosine values are to be calculated. The cosine values must be in the range -1 to 1.
    :param result: Name of the resulting column where the arccosine values will be stored.
    """
    import numpy as np

    df[result] = np.arccos(df[numeric_col])

    return df
