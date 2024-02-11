def capitalize(df, some_col: str, result: str):
    """
    Capitalizes the first letter in a text string
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.capitalize()

    return df
