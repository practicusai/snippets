def cot(df, some_numeric_col: str, result: str):
    """
    Calculates the cotangent of the values in a specified column, and adds the result as a new column to the DataFrame.
    :param some_numeric_col: Name of the column whose values are to be used for cotangent calculation.
    :param result: Name of the resulting column where the cotangent values will be stored.
    """
    import numpy as np
    df[result] = 1 / np.tan(df[some_numeric_col])

    return df
