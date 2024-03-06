def heaviside(df, numeric_col: str, x2: float, result: str):
    """
    Applies the Heaviside step function to values in a column.
    :param numeric_col: Name of the column to apply the function to.
    :param x2: The value of the function when the input is 0. Must be a float.
    :param result: Name of the resulting column where the Heaviside step function values will be stored. 
    """

    import numpy as np

    df[result] = np.heaviside(df[numeric_col], x2)
    return df

