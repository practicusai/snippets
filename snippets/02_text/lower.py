def lower(df, some_col: str, result: str):
    """
    Converts text to lowercase
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.lower()

    return df
