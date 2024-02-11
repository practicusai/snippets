def is_decimal(df, some_col: str, result: str):
    """
    Checks whether all characters are decimal
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.isdecimal()

    return df
