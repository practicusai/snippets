def cosh(df, some_numeric_col: str, result: str):
    """
    Calculates the hyperbolic cosine of the values in a specified column, and adds the result as a new column to the DataFrame.
    :param some_numeric_col: Name of the column whose values are to be used for hyperbolic cosine calculation.
    :param result: Name of the resulting column where the hyperbolic cosine values will be stored.
    """
    import numpy as np
    df[result] = np.cosh(df[some_numeric_col])

    return df

