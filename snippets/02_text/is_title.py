def is_title(df, some_col: str, result: str):
    """
    Checks if the string is title cased.
    Title cased means when a string has the first character in each word uppercase and remaining all characters lowercase alphabets
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.istitle()

    return df
