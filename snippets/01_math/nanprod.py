def nanprod(df, some_col: str, result: str):
    """
    Calculates the product of elements in a column, treating empty values as ones.
    :param some_col: The name of the column to calculate the product over.
    :param result: Resulting column name
    """

    import numpy as np

    df[result] = np.nanprod(df[some_col])

    return df
