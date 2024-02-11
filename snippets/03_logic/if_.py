def if_(df, condition_col: str, if_true_col: str, if_false_col: str, result: str):
    """
    If else logic. Compares the condition and assigns a column value.
    :param condition_col: A logical (boolean) column with True or False values
    :param if_true_col: Column value to use if condition is True
    :param if_false_col: Column value to use if condition is True
    :param result: Resulting column name
    """
    import numpy as np

    df[result] = np.where(df[condition_col], df[if_true_col], df[if_false_col])

    return df
