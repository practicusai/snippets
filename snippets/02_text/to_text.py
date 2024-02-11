def to_text(df, some_col: str, result: str):
    """
    Converts to text (string)
    :param some_col: Column to use
    :param result: Resulting column name
    """
    df[result] = df[some_col].astype(str)

    return df
