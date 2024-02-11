def lstrip(df, some_col: str, text: str | None = None, result: str = ""):
    """
    Removes leading characters such as whitespace or new lines from left side.
    :param some_col: Column to use
    :param text: Text item to strip from left. Default is None
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.lstrip(text)

    return df
