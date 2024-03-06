def capitalize(df, some_text_col: str, result: str):
    """
    This function capitalizes the first letter of each element in the specified column of the DataFrame and creates a new column with the capitalized strings.    :param some_col: Column to calculate
    :param some_text_col: Name of the column containing the text strings.
    :param result: Name of the resulting column with the capitalized strings.
    """
    df[result] = df[some_text_col].str.capitalize()

    return df
