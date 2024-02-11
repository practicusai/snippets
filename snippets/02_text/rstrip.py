def rstrip(df, some_col: str, text: str | None = None, result: str = ""):
    """
    Removes leading characters such as whitespace or new lines from right side.
    :param some_col: Column to use
    :param text: Text item to strip from right. Default is None
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.rstrip(text)

    return df
