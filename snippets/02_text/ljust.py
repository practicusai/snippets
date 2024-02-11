def ljust(df, some_col: str, width: int, fill_char: str = " ", result: str = ""):
    """
    Pads the right side of string
    :param some_col: Column to calculate
    :param width: Minimum width of resulting string; additional characters will be filled with fill_char
    :param fill_char: Additional character for filling, default is whitespace " "
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.rjust(width, fill_char)

    return df
