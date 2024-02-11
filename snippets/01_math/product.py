def prod(df, some_col: str, result: str):
    """
    Product. Multiplies values of a column
    :param some_col: The name of the column to multiply values from.
    :param result: Resulting column name
    """

    import numpy as np
    
    df[result] = np.prod(df[some_col].values, axis=1)

    return df
