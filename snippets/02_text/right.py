def right(df, some_col: str, number_of_characters: int, result: str):
    """
    Returns the last characters in a text string, based on the number of characters you specify
    :param some_col: Column to calculate
    :param number_of_characters: Specifies the number of characters you want to extract
    :param result: Resulting column name
    """
    df[result] = df[some_col].str[-number_of_characters:]

    return df
