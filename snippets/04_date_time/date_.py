def date_(df, year_col: str, month_col: str, day_col: str, result: str):
    """
    Returns the date for provided values
    :param year_col: The year to use
    :param month_col: The month to use
    :param day_col: The day to use
    :param result: Resulting column name
    """
    import pandas as pd

    df[result] = pd.to_datetime(df[[year_col, month_col, day_col]])

    return df
