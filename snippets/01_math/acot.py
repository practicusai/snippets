def acot(df, numeric_col: str, result: str):
    """
    Calculates the principal value of the arccotangent of the values in a specified column 
    and adds the result as a new column to the DataFrame.

    :param numeric_col: Name of the column whose arccotangent values are to be calculated.
    :param result: Name of the resulting column where the arccotangent values will be stored.
    """
    import numpy as np

    df[result] = np.pi/2 - np.arctan(df[numeric_col])

    return df
