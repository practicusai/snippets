def ceil(df, some_col: str, result: str):
    """
    Return the ceiling of the input, element-wise.
    The ceil of the scalar x is the smallest integer i, such that i >= x.
    :param some_col: Column the calculate
    :param result: Resulting column name
    """
    import numpy as np
    df[result] = np.ceil(df[some_col])

    return df
