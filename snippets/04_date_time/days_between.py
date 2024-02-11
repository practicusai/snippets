def days_between(df, begin_date_col: str, end_date_col: str, result: str):
    """
    Returns the number of days between two dates.
    Calculates: End date - Begin date
    :param begin_date_col: Begin date (earlier)
    :param end_date_col: End date (later)
    :param result: Resulting column name
    """

    df[result] = (df[end_date_col] - df[begin_date_col]).dt.day

    return df
