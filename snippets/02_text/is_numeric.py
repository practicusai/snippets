def is_numeric(df, some_text_col: str, result: str):
    """
    Checks if all characters in the string are numeric characters
    :param some_text_col: Name of the column to check for numeric characters.
    :param result: Name of the resulting column containing boolean values indicating
                   whether each value in the column consists of numeric characters.
    """
    df[result] = df[some_text_col].str.isnumeric()

    return df
