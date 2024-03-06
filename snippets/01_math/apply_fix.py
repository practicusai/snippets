def apply_fix(df, some_numeric_col: str, result: str):
    """
    Applies the fix function to round elements of a column in the DataFrame to the nearest integer toward zero,
    and adds the result as a new column to the DataFrame.
    :param some_numeric_col: Column to apply fix operation
    :param result: Name of the resulting column where the fixed values will be stored.
    """
    import numpy as np

    df[result] = np.fix(df[some_numeric_col])

    return df
