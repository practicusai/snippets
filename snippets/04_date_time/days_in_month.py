def days_in_month(df, some_date_col: str, result: str):
    """
    Returns the number of days (1 to 31) of the selected date column
    :param some_date_col: A date column
    :param result: Resulting column name
    """

    df[result] = df[some_date_col].dt.daysinmonth

    return df
