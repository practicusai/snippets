def case_fold(df, some_col: str, result: str):
    """
    Return a case folded copy of the string, e.g., German ß becomes ss.
    :param some_col: Column to calculate
    :param result: Resulting column name
    """

    df[result] = df[some_col].str.casefold()
    return df
