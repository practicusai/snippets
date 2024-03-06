def mid(df, text_col: str, start_position: int, number_of_characters: int, result: str):
    """
    This function extracts a specified number of characters from each string in the specified column of the DataFrame, starting at the position specified by the start_position parameter.
    :param text_col: Name of the column containing strings to extract characters from.
    :param start_position: The zero-based index of the starting position to extract characters from.
    :param number_of_characters: The number of characters to extract from each string.
    :param result: Name of the resulting column containing the extracted characters.
    """
    df[result] = df[text_col].str.slice(start_position, start_position + number_of_characters)

    return df
