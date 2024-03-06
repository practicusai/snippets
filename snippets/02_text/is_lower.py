def is_lower(df, some_text_col: str, result: str):
    """
    This function checks whether each value in the specified column of the DataFrame consists only of lowercase letters.
    :param some_text_col: Name of the column to check for lowercase letters.
    :param result: Name of the resulting column containing boolean values indicating
                   whether each value in the column consists of lowercase letters.
    """
    df[result] = df[some_text_col].str.islower()

    return df
