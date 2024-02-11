def is_upper(df, some_col: str, result: str):
    """
    Checks if all characters in the string are uppercase.
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.isupper()

    return df
