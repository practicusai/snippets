def product(df, numeric_col: str, result: str):
    """
    Calculates the product of values in a column.
    :param numeric_col: Name of the column to calculate the product over.
    :param result: Name of the resulting column where the product value will be stored.
    """

    import numpy as np
    
    df[result] = np.prod(df[numeric_col].values, axis=1)

    return df
