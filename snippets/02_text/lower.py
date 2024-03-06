def lower(df, some_text_col: str, result: str):
    """
    This function converts all characters in the specified column to lowercase.
    It operates on string-type columns only.
    :param some_text_col: Name of the column containing text to be converted to lowercase.
    :param result: Name of the resulting column containing the lowercase text.
    """
    df[result] = df[some_text_col].str.lower()

    return df
