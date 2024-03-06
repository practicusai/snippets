def zfill(df, some_text_col: str, width: int, result: str = ""):
    """
    Pad strings in the text by prepending ‘0’ characters.
    :param some_text_col: Name of the column containing the values to be padded.
    :param width: Minimum width of resulting string; additional characters will be filled with fill_char
    :param result: Name of the resulting column containing the padded values.
    """
    df[result] = df[some_text_col].str.zfill(width)

    return df
