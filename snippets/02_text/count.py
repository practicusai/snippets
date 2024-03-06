def count(df, text_col: str, pattern: str, flags: int = 0, result: str = ""):
    """
    This function counts the occurrences of the specified regular expression pattern in each string of the specified column in the DataFrame.   
    :param text_col: Name of the column to count pattern occurrences in.
    :param pattern: Regular expression pattern to count occurrences of.
    :param flags: Flags for the regular expression module. Default is 0.
    :param result: Name of the resulting column containing the count of occurrences. 
                   If not provided, a new column will be created with a default name.
    """

    df[result] = df[text_col].str.count(pattern, flags=flags)
    return df
