def arctan(df, some_col: str, result: str):
    """
    Returns the arctangent, or inverse tangent, of a number. The arctangent is the angle whose tangent is number.
    The returned angle is given in radians in the range -pi/2 to pi/2.
    :param some_col: Colum to calculate
    :param result: Resulting column name
    """
    import numpy as np
    df[result] = np.arctan(df[some_col])

    return df
