def right(df, some_text_col: str, number_of_characters: int, result: str):
    """
This function extracts the specified number of characters from the end of each string in the specified column of the DataFrame and stores the result in a new column.
    :param some_text_col: Name of the column containing text strings to extract characters from.
    :param number_of_characters: Number of characters to extract from the end of each string.
    :param result: Name of the resulting column containing the extracted characters.
    """
    df[result] = df[some_text_col].str[-number_of_characters:]

    return df
