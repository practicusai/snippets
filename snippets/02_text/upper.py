def upper(df, some_col: str, result: str):
    """
    Converts text to uppercase
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.upper()

    return df
