def is_alpha(df, some_col: str, result: str):
    """
    Checks whether all the characters in a given string are alphabets
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.isalpha()

    return df
