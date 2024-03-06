def cov(df, some_numeric_col: list[str], result: str):
    """
    Calculates the covariance of selected columns for each row separately.
    This is a row based operation. To calculate for all columns, please use "Group by" under Analyze menu
    :param some_numeric_col: Columns with numeric values
    :param result: Resulting column name
    """
    df[result] = df[some_numeric_col].cov(axis=1)

    return df
