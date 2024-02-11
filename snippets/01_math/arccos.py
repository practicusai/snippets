def arccos(df, some_col: str, result: str):
    """
    Returns the arccosine, or inverse cosine, of a number. The arccosine is the angle whose cosine is number. The returned angle is given in radians in the range 0 (zero) to pi.
    :param some_col: Required. The cosine of the angle you want and must be from -1 to 1.
    :param result: Resulting column name
    """
    import numpy as np

    df[result] = np.arccos(df[some_col])

    return df
