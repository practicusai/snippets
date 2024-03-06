def endswith(df, some_text_col: str, text: str, result: str):
    """
    This function checks if the end of each string element in the specified column of the DataFrame matches the given text or any of the strings in the tuple.
    :param some_text_col: Name of the column containing the string elements to be checked.
    :param text: Character sequence or tuple of strings to check for at the end of each string.
    :param result: Name of the resulting column containing the boolean result. 
                   If not provided, a new column will be created with a default name.
    """

    df[result] = df[some_text_col].str.endswith(text)
    return df
