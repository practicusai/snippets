def lstrip(df, text_col: str, text: str | None = None, result: str = ""):
    """
    This function removes leading characters, which may include whitespace or specific text, from the left side of each string in the specified column of the DataFrame.    
    :param text_col: Name of the column containing strings to be stripped.
    :param text: Optional. The specific text item to strip from the left side of each string.
                 If not provided, leading whitespace will be stripped. Default is None.
    :param result: Name of the resulting column containing the stripped strings.
    """
    df[result] = df[text_col].str.lstrip(text)

    return df
