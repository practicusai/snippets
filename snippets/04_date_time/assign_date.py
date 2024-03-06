from datetime import date


def assign_date(df, datetime_col: date, result: str = ""):
    """
    Assigns a static date to the selected column
    :param datetime_col: Pick a date
    :param result: Resulting column name
    """
    import pandas as pd

    df[result] = pd.to_datetime(datetime_col)

    return df
