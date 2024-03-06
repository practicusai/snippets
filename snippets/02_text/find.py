def find(df, some_text_col: str, text_to_find: str, start_pos: int = None, end_pos: int | None = None, result: str = ""):
    """
    This function searches each string element in the specified column of the DataFrame for the specified text and returns the lowest index (number) where the text is found. If the text is not found, -1 is returned.    
    :param some_text_col: Name of the column containing the string elements to search within.
    :param text_to_find: The string to search for within each string element.
    :param start_pos: Optional. The position in the string to start the search from. Default is None,
                      which means the search will start from the beginning of each string.
    :param end_pos: Optional. The position in the string to end the search at. Default is None,
                    which means the search will continue to the end of each string.
    :param result: Optional. Name of the resulting column containing the indexes where the text is found.
                   If not provided, a new column will be created with a default name.
    """
    df[result] = df[some_text_col].str.find(text_to_find, start_pos, end_pos)

    return df
