def replace(df, some_text_col: str, old_text: str, new_text: str, regular_expression: bool = False, result: str = ""):
    """
This function replaces occurrences of the specified text pattern with another text pattern in each cell of the specified column in the DataFrame and stores the result in a new column.
    :param some_text_col: Name of the column containing text to replace patterns in.
    :param old_text: Text pattern to be replaced.
    :param new_text: Text pattern to replace occurrences of old_text.
    :param regular_expression: Whether to interpret old_text as a regular expression pattern. Default is False.
    :param result: Name of the resulting column containing the replaced text.
    """
    df[result] = df[some_text_col].str.replace(old_text, new_text, regex=regular_expression)

    return df
