def is_alpha(df, some_text_col: str, result: str):
    """
    This function checks whether all characters in each string element of the specified column of the DataFrame are alphabetic (i.e., alphabetical letters) and returns True if they are, otherwise returns False.
    :param some_text_col: Name of the column containing the string elements to check.
    :param result: Name of the resulting column containing the boolean values indicating
                   whether each string element consists entirely of alphabetic characters.
    """
    df[result] = df[some_text_col].str.isalpha()

    return df
