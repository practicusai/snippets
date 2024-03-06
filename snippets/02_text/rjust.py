def rjust(df, some_text_col: str, width: int, fill_char: str = " ", result: str = ""):
    """
    Pads the left side of string
    :param some_text_col: Name of the column containing text strings to be padded.
    :param width: Minimum width of the resulting string after padding.
    :param fill_char: Character used for filling, default is whitespace (" ").
    :param result: Name of the resulting column containing the padded strings.
    """
    df[result] = df[some_text_col].str.rjust(width, fill_char)

    return df
