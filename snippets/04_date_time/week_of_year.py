def week_of_year(df, datetime_col: str, result: str):
    """
    Returns the week of the year of a date column
    :param datetime_col: A date column
    :param result: Resulting column name
    """
    df[result] = df[datetime_col].dt.isocalendar().week.astype(int)

    return df
