def assign_text(df, some_text: str, result: str):
    """
    Assigns a static text (string)
    :param some_text: A static string to assign
    :param result: Resulting column name
    """
    df[result] = some_text

    return df
