def strip(df, some_text_col: str, result: str):
    """
    Returns a copy with the leading and trailing characters removed
    :param some_text_col: Name of the column to remove leading and trailing characters from.
    :param result: Name of the resulting column containing the modified string elements.
    """
    import numpy as np

    df[result] = np.char.strip(df[some_text_col])

    return df
