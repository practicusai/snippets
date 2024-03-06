def or_(df, condition_bool_col: list[str], result: str):
    """
    Logical OR. Returns True if ANY of selected columns is True, or else returns False
    :param condition_col: Logical (boolean) columns with True or False values
    :param result: Resulting column name
    """
    import numpy as np

    combined_result = df[condition_bool_col[0]]
    for i in range(1, len(condition_bool_col)):
        combined_result = np.logical_or(combined_result, df[condition_bool_col[i]])

    df[result] = combined_result

    return df
