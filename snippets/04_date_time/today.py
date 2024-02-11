def today(df, result: str):
    """
    Returns the current date and time
    :param result: Resulting column name
    """
    import pandas as pd

    df[result] = pd.Timestamp.today().normalize()

    return df
