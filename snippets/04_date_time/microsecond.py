def microsecond(df, datetime_col: str, result: str):
    """
    Returns the microseconds of the selected date column
    :param datetime_col: A date column
    :param result: Resulting column name
    """
    df[result] = df[datetime_col].dt.microsecond

    return df
