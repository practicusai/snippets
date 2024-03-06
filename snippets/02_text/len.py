def len(df, text_col: str, result: str):
    """
    Calculates the length of each text string in a column.
    :param text_col: Name of the column containing the text strings.
    :param result: Name of the resulting column containing the length of each string.
    """
    df[result] = df[text_col].str.len()

    return df
