def now(df, result: str):
    """
    Returns the current date and time
    :param result: Resulting column name
    """
    import pandas as pd

    df[result] = pd.Timestamp.now()

    return df
