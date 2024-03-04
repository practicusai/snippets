def replace_empty(df, some_col: str, replacement_value: object, result: str):
    """
    Replaces empty (None) values in a column with a specified number.
    :param some_col: The name of the column to replace empty values in.
    :param replacement_value: The value empty values with.
    :param result: Resulting column name
    """
    df[result if result else some_col] = df[some_col].fillna(replacement_value)

    return df
