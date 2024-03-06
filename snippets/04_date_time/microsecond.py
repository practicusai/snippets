def microsecond(df, some_date_col: str, result: str):
    """
    Returns the microseconds of the selected date column
    :param some_date_col: A date column
    :param result: Resulting column name
    """
    df[result] = df[some_date_col].dt.microsecond

    return df
