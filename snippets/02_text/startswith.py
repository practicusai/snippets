def startswith(df, some_col: str, text: str, result: str):
    """
    Test if the start of each string element matches the text.
    :param some_col: Column to use
    :param text: Character sequence or tuple of strings.
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.startswith(text)

    return df
