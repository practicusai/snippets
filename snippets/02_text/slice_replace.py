def slice_replace(df, some_col: str, start: int, stop: int, replacement: str, result: str):
    """
    Replace a positional slice of a string with another value
    :param some_col: Column to use
    :param start: Start position for slice operation.
    :param stop: Stop position for slice operation.
    :param replacement: String for replacement
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.slice_replace(start, stop, replacement)

    return df
