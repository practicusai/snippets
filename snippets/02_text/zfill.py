def zfill(df, some_col: str, width: int, result: str = ""):
    """
    Pad strings in the text by prepending ‘0’ characters.
    :param some_col: Column to calculate
    :param width: Minimum width of resulting string; additional characters will be filled with fill_char
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.zfill(width)

    return df
