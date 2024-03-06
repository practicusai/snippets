from datetime import datetime


def assign_datetime(df, datetime_col: datetime, result: str = ""):
    """
    Assigns a static date and time to the selected column
    :param datetime_col: Pick a date and time
    :param result: Resulting column name
    """
    import pandas as pd

    df[result] = pd.to_datetime(datetime_col)

    return df
