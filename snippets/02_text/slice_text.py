def slice_text(df, some_col: str, start: int, stop: int, step: int, result: str):
    """
    Slice substrings from each element in the text.
    :param some_col: Column to use
    :param start: Start position for slice operation.
    :param stop: Stop position for slice operation.
    :param step: Step size for slice operation.
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.slice(start, stop, step)

    return df
