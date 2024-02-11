def is_blank(df, some_col: str, result: str):
    """
    Returns True if value is blank, False otherwise
    :param some_col: Column to check
    :param result: Resulting column name
    """
    import pandas as pd
    df[result] = pd.isna(df[some_col])

    return df
