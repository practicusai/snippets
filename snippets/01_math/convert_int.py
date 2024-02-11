def convert_int(df, some_col: str, result: str):
    """
    Rounds numbers down to the nearest integer in a column.
    :param some_col: The name of the column to round down.
    :param result: Resulting column name
    """
    import numpy as np

    df[result] = np.floor(df[some_col]).astype(int)
    return df

