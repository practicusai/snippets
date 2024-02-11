def heaviside(df, some_col: str, x2: float = 0.5, result: str = "heaviside"):
    """
    Applies the Heaviside step function to values in a column.
    :param some_col: The name of the column to apply the function to.
    :param x2: The value of the function when x1 is 0
    :param result: Resulting column name
    """

    import numpy as np

    df[result] = np.heaviside(df[some_col], x2)
    return df

