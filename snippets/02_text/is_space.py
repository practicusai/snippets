def is_space(df, some_col: str, result: str):
    """
    Checks whether all the characters in a given string are spaces
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.isspace()

    return df
