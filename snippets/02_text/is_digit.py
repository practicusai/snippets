def is_digit(df, some_col: str, result: str):
    """
    Checks whether all the characters in a given string are numbers such as 0123456789
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.isdigit()

    return df
