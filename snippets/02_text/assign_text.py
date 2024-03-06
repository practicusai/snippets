def assign_text(df, some_text_col: str, result: str):
    """
    This function assigns the specified static text to a new column in the DataFrame.
    :param some_text_col: A static string to assign to the new column.
    :param result: Resulting column name for the new column with the assigned text.
    """
    df[result] = some_text_col

    return df
