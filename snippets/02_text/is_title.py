def is_title(df, some_text_col: str, result: str):
    """
    Checks if the string is title cased.
    Title cased means when a string has the first character in each word uppercase and remaining all characters lowercase alphabets
    :param some_text_col: Name of the column to check for title cased strings.
    :param result: Name of the resulting column containing boolean values indicating
                   whether each value in the column is title cased.
    """
    df[result] = df[some_text_col].str.istitle()

    return df
