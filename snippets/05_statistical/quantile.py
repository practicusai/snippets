def quantile(df, numeric_col_list: list[str], q: float = 0.5, result: str = ""):
    """
    Calculates the variance of selected columns for each row separately.
    This is a row based operation. To calculate for all columns, please use "Group by" under Analyze menu
    :param numeric_col_list: Columns with numeric values
    :param q: Quantile 0 to 1. E.g. 0.5 is 50%
    :param result: Resulting column name
    """
    df[result] = df[numeric_col_list].quantile(axis=1, q=q)

    return df
