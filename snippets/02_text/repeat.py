def repeat(df, some_col: str, count: int, result: str):
    """
    Repeats the text a given number of times.
    :param some_col: Column to use
    :param count: Number times to repeat
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.repeat(count)

    return df
