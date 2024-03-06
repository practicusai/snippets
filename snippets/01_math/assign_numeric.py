def assign_numeric(df, some_number: float, result: str):
    """
    Assigns a static integer or decimal number.
    :param some_number: A static integer or decimal number to be assigned.
    :param result: Name of the resulting column where the number will be stored.
    """
    df[result] = some_number

    if some_number == int(some_number):
        df[result] = df[result].astype(int)

    return df
