def arctanh(df, some_numeric_col: str, result: str):
    """
    Calculates the inverse hyperbolic tangent of the values in a specified column, and adds the result as a new column to the DataFrame.    
    :param some_numeric_col: Name of the column whose hyperbolic tangent values are to be calculated.
    :param result: Name of the resulting column where the arctanh values will be stored.
    """
    import numpy as np
    df[result] = np.arctanh(df[some_numeric_col])

    return df
