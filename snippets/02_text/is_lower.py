def is_lower(df, some_col: str, result: str):
    """
    Checks if all characters in the string are lowercase.
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.islower()

    return df
