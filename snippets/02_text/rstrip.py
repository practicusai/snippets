def rstrip(df, some_text_col: str, text: str | None = None, result: str = ""):
    """
This function removes trailing characters (specified by the `text` parameter) from the right side of each string in the specified column of the DataFrame. If `text` is not provided, it removes trailing whitespace by default.
    :param some_text_col: Name of the column containing text strings to be stripped.
    :param text: Text item to strip from the right side. If None, removes trailing whitespace (default is None).
    :param result: Name of the resulting column containing the stripped strings.
    """
    df[result] = df[some_text_col].str.rstrip(text)

    return df
