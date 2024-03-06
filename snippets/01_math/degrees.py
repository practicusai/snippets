def degrees(df, numeric_col: str, result: str):
    """
    Converts the values in a specified column from radians to degrees, and adds the result as a new column to the DataFrame. 
    Values in the specified column should be in radians.
    :param numeric_col: Name of the column whose values are in radians and to be converted to degrees. Values in this column should be in radians.
    :param result: Name of the resulting column where the degree values will be stored.
    """
    import numpy as np
    df[result] = np.degrees(df[numeric_col])

    return df
