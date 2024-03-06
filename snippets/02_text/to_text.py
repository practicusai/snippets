def to_text(df, text_col: str, result: str):
    """
    This function converts the values in the specified column of the DataFrame to text (string) format, ensuring that all values are represented as strings.
    :param text_col: Name of the column containing the values to be converted.
    :param result: Name of the resulting column containing the values converted to text format.
    """
    df[result] = df[text_col].astype(str)

    return df
