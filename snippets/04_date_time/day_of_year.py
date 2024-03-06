def day_of_year(df, datetime_col_list: list[str], result: str):
    """
    Returns the ordinal day of the year
    :param datetime_col_list: A date column
    :param result: Resulting column name
    """

    df[result] = df[datetime_col_list].dt.dayofyear

    return df
