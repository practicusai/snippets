def is_alphanumeric(df, some_col: str, result: str):
    """
    Checks whether all the characters in a given string are alphanumeric or not.
    Alphanumeric means a character that is either a letter or a number.
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.isalnum()

    return df
