def arccosh(df, numeric_col: str, result: str):
    """
    Calculates the inverse hyperbolic cosine (arccosh) of the values in a specified column,
    and adds the result as a new column to the DataFrame.
    :param numeric_col: Name of the column whose hyperbolic cosine values are to be calculated.
    :param result: Name of the resulting column where the arccosh values will be stored.
    """
    import numpy as np

    df[result] = np.arccosh(df[numeric_col])

    return df

