def upper(df, some_text_col: str, result: str):
    """
    This function converts all characters in the values of the specified column to uppercase.
    :param some_text_col: Name of the column containing the values to be converted to uppercase.
    :param result: Name of the resulting column containing the uppercase values.
    """
    df[result] = df[some_text_col].str.upper()

    return df
