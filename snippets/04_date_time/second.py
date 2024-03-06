def second(df, some_date_col: str, result: str):
    """
    Returns the second of the selected date column
    :param some_date_col: A date column
    :param result: Resulting column name
    """
    df[result] = df[some_date_col].dt.second

    return df
