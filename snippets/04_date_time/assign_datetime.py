from datetime import datetime


def assign_datetime(df, some_datetime: datetime, result: str = ""):
    """
    Assigns a static date and time to the selected column
    :param some_datetime: Pick a date and time
    :param result: Resulting column name
    """
    import pandas as pd

    df[result] = pd.to_datetime(some_datetime)

    return df
