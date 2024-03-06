def arctan(df, numeric_col: str, result: str):
    """
    Calculates the arctangent of the values in a specified columns, and adds the result as a new column to the DataFrame.    The returned angle is given in radians in the range -pi/2 to pi/2.
    :param numeric_col: Name of the column whose arctangent values are to be calculated.
    :param result: Name of the resulting column where the arctangent values will be stored.
    """
    import numpy as np
    df[result] = np.arctan(df[numeric_col])

    return df
