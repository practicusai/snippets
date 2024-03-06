def startswith(df, text_col: str, text: str, result: str):
    """
    This function checks if the start of each string element in the specified column of the DataFrame matches the specified text.
    :param text_col: Name of the column to check for the start of each string element.
    :param text: Character sequence or tuple of strings to check for at the start of each string element.
    :param result: Name of the resulting column containing the boolean result of the check.
    """
    df[result] = df[text_col].str.startswith(text)

    return df
