def week_of_year(df, some_date_col: str, result: str):
    """
    Returns the week of the year of a date column
    :param some_date_col: A date column
    :param result: Resulting column name
    """
    df[result] = df[some_date_col].dt.isocalendar().week.astype(int)

    return df
