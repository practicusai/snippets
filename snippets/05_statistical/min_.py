def min_(df, some_col: list[str], result: str):
    """
    Calculates the min of selected columns for each row separately.
    This is a row based operation. To calculate for all columns, please use "Group by" under Analyze menu
    :param some_col: Columns with numeric values
    :param result: Resulting column name
    """
    df[result] = df[some_col].min(axis=1)

    return df
