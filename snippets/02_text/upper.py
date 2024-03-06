def upper(df, text_col: str, result: str):
    """
    This function converts all characters in the values of the specified column to uppercase.
    :param text_col: Name of the column containing the values to be converted to uppercase.
    :param result: Name of the resulting column containing the uppercase values.
    """
    df[result] = df[text_col].str.upper()

    return df
