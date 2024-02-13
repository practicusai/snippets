from datetime import date


def assign_date(df, some_date: date, result: str = ""):
    """
    Assigns a static date to the selected column
    :param some_date: Pick a date
    :param result: Resulting column name
    """
    import pandas as pd

    df[result] = pd.to_datetime(some_date)

    return df
