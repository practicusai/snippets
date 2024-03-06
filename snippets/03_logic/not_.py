def not_(df, condition_bool_col: list[str], result: str):
    """
    Logical NOT. Returns True if column value is False, And False if column value is True
    :param condition_bool_col: Logical (boolean) column with True or False value
    :param result: Resulting column name
    """
    import numpy as np

    df[result] = np.logical_not(df[condition_bool_col])

    return df
