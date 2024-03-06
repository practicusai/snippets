def left(df, text_col: str, number_of_characters: int, result: str):
    """
    Returns the first characters in a text string, based on the number of characters you specify
    :param text_col: Name of the column containing the text strings.
    :param number_of_characters: Number of characters to extract from the beginning of each string.
    :param result: Name of the resulting column containing the extracted characters.
    """
    df[result] = df[text_col].str[:number_of_characters]

    return df
