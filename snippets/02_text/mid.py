def mid(df, some_col: str, start_position: int, number_of_characters: int, result: str):
    """
    Returns a specific number of characters from a text string, starting at the position you specify
    :param some_col: Column to calculate
    :param start_position: Specifies the start position to extract (start with 0)
    :param number_of_characters: Specifies the number of characters you want to extract
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.slice(start_position, start_position + number_of_characters)

    return df
