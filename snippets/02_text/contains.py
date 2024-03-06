def contains(df, text_col: str, pattern: str, case: bool = True, flags: int = 0, na: str | None = None,
             regular_expression: bool = True, result: str = ""):
    """
    This function checks if the specified pattern or regular expression is contained within each string in the specified column of the DataFrame. 
    It returns True for rows where the pattern or regular expression is found and False otherwise.        
    :param text_col: Name of the column to check for the pattern or regular expression.
    :param pattern: The pattern or regular expression to search for.
    :param case: Whether to perform a case-sensitive match. Default is True.
    :param flags: Flags to pass through to the regular expression module, e.g., to ignore case. Default is 0.
    :param na: How to handle missing values. Options are None (default), 'NA', or '', where None indicates
               missing values should be kept, 'NA' indicates missing values should be considered False,
               and '' indicates missing values should be considered True.
    :param regular_expression: Whether the pattern is a regular expression. Default is True.
    :param result: Name of the resulting column with boolean values indicating whether the pattern was found.
                   If not provided, a new column will be created with a default name.
    """
    df[result] = df[text_col].str.contains(pattern, case=case, flags=flags, na=na, regex=regular_expression)
    return df
