def is_numeric(df, some_col: str, result: str):
    """
    Checks if all characters in the string are numeric characters
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.isnumeric()

    return df
