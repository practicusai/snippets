def title(df, text_col: str, result: str):
    """
    Converts the first character in each word to uppercase
    :param text_col: Name of the column to convert to title case.
    :param result: Name of the resulting column containing the title-cased string elements.
    """
    df[result] = df[text_col].str.title()

    return df
