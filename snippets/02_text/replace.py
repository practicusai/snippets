def replace(df, some_col: str, old_text: str, new_text: str, regular_expression: bool = False, result: str = ""):
    """
    Replaces part of a text string with another string
    :param some_col: Column to calculate
    :param old_text: Text to replace
    :param new_text: Text to replace with
    :param regular_expression: Enable advanced pattern matching
    :param result: Resulting column name
    """
    df[result] = df[some_col].str.replace(old_text, new_text, regex=regular_expression)

    return df
