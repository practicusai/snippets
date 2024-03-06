def ceil(df, some_numeric_col: str, result: str):
    """
    Calculates the ceiling of the values in a specified column, and adds the result as a new column to the DataFrame.
    The ceiling of a scalar x is the smallest integer i such that i >= x.
    :param some_numeric_col: Name of the column whose values are to be calculated.
    :param result: Name of the resulting column where the ceiling values will be stored.
    """
    import numpy as np
    df[result] = np.ceil(df[some_numeric_col])

    return df
