def assign_boolean(df, some_bool: bool, result: str):
    """
    Assigns a static boolean value (True or False)
    :param some_bool: A boolean value
    :param result: Resulting column name
    """
    df[result] = some_bool

    return df
