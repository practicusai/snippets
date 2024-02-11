def find(df, some_col: str, text_to_find: str, start_pos: int = None, end_pos: int | None = None, result: str = ""):
    """
    Returns the lowest indexes (number) of the
    :param some_col: Column to use
    :param text_to_find: The string you are searching
    :param start_pos: Column to use
    :param end_pos: Column to use
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.find(text_to_find, start_pos, end_pos)

    return df
