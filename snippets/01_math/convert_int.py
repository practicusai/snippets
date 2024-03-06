def convert_int(df, some_numeric_col: str, result: str):
    """
    Converts the values in a specified column to integers by rounding them down to the nearest integer.
    :param some_numeric_col: Name of the column whose values are to be converted to integers.
    :param result: Name of the resulting column where the converted integer values will be stored.
    """
    import numpy as np

    df[result] = np.floor(df[some_numeric_col]).astype(int)
    return df

