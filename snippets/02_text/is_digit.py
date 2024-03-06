def is_digit(df, text_col: str, result: str):
    """
    Checks whether all the characters in a given string are numbers such as 0123456789
    :param text_col: Name of the column to check for digit values.
    :param result: Name of the resulting column containing boolean values indicating whether each value in the column consists of digit characters.
    """
    df[result] = df[text_col].str.isdigit()

    return df
