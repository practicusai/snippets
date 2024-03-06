def nanprod(df, some_numeric_col: str, result: str):
    """
    Calculates the product of elements in a column, treating empty values as ones.
    :param some_numeric_col: Name of the column to calculate the product over.
    :param result: Name of the resulting column where the product value will be stored.
    """

    import numpy as np

    df[result] = np.nanprod(df[some_numeric_col])

    return df
