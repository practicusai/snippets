def count(df, some_col: str, pattern: str, flags: int = 0, result: str = ""):
    """
    Count occurrences of pattern in each string
    :param some_col: Column to use
    :param pattern: A regular expression pattern
    :param flags: Flags for the regular expression module.
    :param result: Resulting column name
    """

    df[result] = df[some_col].str.count(pattern, flags=flags)
    return df
