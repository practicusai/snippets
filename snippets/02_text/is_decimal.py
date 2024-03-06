def is_decimal(df, some_text_col: str, result: str):
    """
    This function checks whether each value in the specified column of the DataFrame consists only of decimal characters (0-9).
    :param some_text_col: Name of the column to check for decimal values.
    :param result: Name of the resulting column containing boolean values indicating whether each value in the column consists of decimal characters.
    """
    df[result] = df[some_text_col].str.isdecimal()

    return df
