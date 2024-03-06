def max_(df, numeric_col_list: list[str], result: str):
    """
    Calculates the max of selected columns for each row separately.
    This is a row based operation. To calculate for all columns, please use "Group by" under Analyze menu
    :param numeric_col_list: Columns with numeric values
    :param result: Resulting column name
    """
    df[result] = df[numeric_col_list].max(axis=1)

    return df
