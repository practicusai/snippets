def title(df, some_col: str, result: str):
    """
    Converts the first character in each word to uppercase
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.title()

    return df
