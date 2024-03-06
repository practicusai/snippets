def arcsin(df, numeric_col: str, result: str):
    """
    Returns the arcsine, or inverse sine, of a number. The arcsine is the angle whose sine is the specified number.
    The returned angle is given in radians in the range -π/2 to π/2.
    :param numeric_col: Name of the column whose sine values are to be calculated.
    :param result: Name of the resulting column where the arcsine values will be stored.
    """
    import numpy as np
    df[result] = np.arcsin(df[numeric_col])

    return df
