def replace_empty_num(df, numeric_col: str, replacement_value: float, result: str):
    """
    Replaces empty (None) values in a column with a specified number.
    :param numeric_col: Name of the column to replace empty values in.
    :param replacement_value: The value to replace empty values with. Must be float.
    :param result: Name of the resulting column where the values with replacements will be stored.
    """
    df[result if result else numeric_col] = df[numeric_col].fillna(replacement_value)
    return df
