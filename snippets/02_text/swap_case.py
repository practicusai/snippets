def swap_case(df, some_col: str, result: str):
    """
    Converts all uppercase characters to lowercase, and vice versa
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.swapcase()

    return df
