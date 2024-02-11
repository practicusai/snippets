def length(df, some_col: str, result: str):
    """
    Returns the number of characters in a text
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.len()

    return df
