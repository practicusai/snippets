def repeat(df, text_col: str, count: int, result: str):
    """
    Repeats the text a given number of times.
    :param text_col: Name of the column containing text to repeat.
    :param count: Number of times to repeat the text in each cell.
    :param result: Name of the resulting column containing the repeated text.
    """
    df[result] = df[text_col].str.repeat(count)

    return df
