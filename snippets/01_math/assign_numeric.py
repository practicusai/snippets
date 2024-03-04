def assign_numeric(df, some_number: float, result: str):
    """
    Assigns a static integer or decimal number.
    :param some_number: Some integer or decimal number
    :param result: Resulting column name
    """
    df[result] = some_number

    if some_number == int(some_number):
        df[result] = df[result].astype(int)

    return df
