def is_upper(df, some_text_col: str, result: str):
    """
    Checks if all characters in the string are uppercase.
    :param some_text_col: Name of the column to check for uppercase strings.
    :param result: Name of the resulting column containing boolean values indicating
                   whether each value in the column is uppercase.
    """
    df[result] = df[some_text_col].str.isupper()

    return df
