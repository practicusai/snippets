def product(df, some_numeric_col: str, result: str):
    """
    Calculates the product of values in a column.
    :param some_numeric_col: Name of the column to calculate the product over.
    :param result: Name of the resulting column where the product value will be stored.
    """

    import numpy as np
    
    df[result] = np.prod(df[some_numeric_col].values, axis=1)

    return df
