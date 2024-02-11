def contains(df, some_col: str, pattern: str, case: bool = True, flags: int = 0, na: str | None = None,
             regular_expression: bool = True, result: str = ""):
    """
    Test if pattern or regex is contained within a string
    :param some_col: Column to use
    :param pattern: The pattern or regular expression to search for.
    :param case: Whether to perform a case-sensitive match
    :param flags: Flags to pass through to the regular expression module, e.g. to ignore case
    :param na: How to handle missing values, default is None
    :param regular_expression: Enable advanced pattern matching
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.contains(pattern, case=case, flags=flags, na=na, regex=regular_expression)
    return df
