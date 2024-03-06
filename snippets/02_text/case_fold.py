def case_fold(df, some_text_col: str, result: str):
    """
    This function converts the text in the specified column of the DataFrame to lowercase, applying Unicode rules for case folding. 
    For example, the German letter 'ß' will be converted to 'ss'.    
    :param some_text_col: Name of the column containing the text strings.
    :param result: Name of the resulting column with the case folded strings.
    """

    df[result] = df[some_text_col].str.casefold()
    return df
