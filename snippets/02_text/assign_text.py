def assign_text(df, text_col: str, result: str):
    """
    This function assigns the specified static text to a new column in the DataFrame.
    :param text_col: A static string to assign to the new column.
    :param result: Resulting column name for the new column with the assigned text.
    """
    df[result] = text_col

    return df
