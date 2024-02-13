def and_(df, condition_col: list[str], result: str):
    """
    Logical AND. Returns True if ALL selected columns are True, or else returns False
    :param condition_col: Logical (boolean) columns with True or False values
    :param result: Resulting column name
    """
    import numpy as np

    combined_result = df[condition_col[0]]
    for i in range(1, len(condition_col)):
        combined_result = np.logical_and(combined_result, df[condition_col[i]])

    df[result] = combined_result

    return df
