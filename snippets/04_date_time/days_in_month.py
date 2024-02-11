def days_in_month(df, some_col: str, result: str):
    """
    Returns the number of days (1 to 31) of the selected date column
    :param some_col: A date column
    :param result: Resulting column name
    """

    df[result] = df[some_col].dt.daysinmonth

    return df
