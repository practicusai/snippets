def ljust(df, text_col: str, width: int, fill_char: str = " ", result: str = ""):
    """
    Pads the right side of each string in a column with a specified character until the string reaches a specified width.
    :param text_col: Name of the column containing the strings to pad.
    :param width: Minimum width of the resulting strings; additional characters will be filled with fill_char.
    :param fill_char: Additional character for filling. Default is whitespace (" ").
    :param result: Name of the resulting column containing the padded strings. If not provided, the original column will be overwritten.
    """
    df[result] = df[text_col].str.rjust(width, fill_char)

    return df
