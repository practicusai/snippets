def is_space(df, text_col: str, result: str):
    """
    This function checks whether each value in the specified column of the DataFrame consists only of space characters.
    :param text_col: Name of the column to check for space characters.
    :param result: Name of the resulting column containing boolean values indicating
                   whether each value in the column consists of space characters.
    """
    df[result] = df[text_col].str.isspace()

    return df
