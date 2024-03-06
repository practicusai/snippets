def xor(df, condition_bool_col: list[str], result: str):
    """
    Returns a logical exclusive OR of all arguments
    :param condition_col: Logical (boolean) columns with True or False values
    :param result: Resulting column name
    """
    if len(condition_bool_col) < 2:
        raise ValueError("Logical XOR requires 2 or more columns")

    import numpy as np

    combined_result = np.logical_xor(df[condition_bool_col[0]], df[condition_bool_col[1]])
    for i in range(2, len(condition_bool_col)):
        combined_result = np.logical_or(combined_result, df[condition_bool_col[i]])

    df[result] = combined_result

    return df
