def arcsin(df, some_col: str, result: str):
    """
    Returns the arcsine, or inverse sine, of a number. The arcsine is the angle whose sine is number.
    The returned angle is given in radians in the range -pi/2 to pi/2.
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    import numpy as np
    df[result] = np.arcsin(df[some_col])

    return df
