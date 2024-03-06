def pad(df, some_text_col: str, width: int, side: int, fill_char: str = " ", result: str = ""):
    """
    This function pads the strings in the specified column of the DataFrame to a minimum width using the specified fill character. The padding can be applied to the left, right, or both sides of the strings.    
    :param some_text_col: Name of the column containing strings to pad.
    :param width: Minimum width of the resulting strings after padding.
    :param side: Side from which to fill the resulting strings. Can be 'left', 'right', or 'both'.
    :param fill_char: Additional character for filling. Default is whitespace ' '.
    :param result: Name of the resulting column containing the padded strings.
    """

    df[result] = df[some_text_col].str.spad(width, side, fill_char)
    return df
