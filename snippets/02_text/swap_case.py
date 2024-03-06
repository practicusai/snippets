def swap_case(df, text_col: str, result: str):
    """
    This function converts all uppercase characters to lowercase, and vice versa, for each string element
    in the specified column of the DataFrame.
    :param text_col: Name of the column to swap the case of its characters.
    :param result: Name of the resulting column containing the modified string elements.
    """
    df[result] = df[text_col].str.swapcase()

    return df
