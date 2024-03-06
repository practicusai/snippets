def trim(df, some_text_col: str, result: str):
    """
    Removes leading and trailing whitespace characters from the values in a column.
    :param some_text_col: Name of the column containing the values to be trimmed.
    :param result: Name of the resulting column containing the trimmed values.
    """
    import numpy as np

    df[result] = np.char.strip(df[some_text_col])

    return df
