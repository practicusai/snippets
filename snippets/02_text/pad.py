def pad(df, some_col: str, width: int, side: int, fill_char: str = " ", result: str = ""):
    """
    Prepares pad strings in the text
    :param some_col: Column to use
    :param width: Minimum width of resulting string.
    :param side: Side from which to fill resulting string : left, right, both.
    :param fill_char: Additional character for filling, default is whitespace " "
    :param result: Resulting column name
    """

    df[result] = df[some_col].str.spad(width, side, fill_char)
    return df
