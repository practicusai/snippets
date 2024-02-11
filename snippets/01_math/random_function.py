def random_function(df, result: str):
    """
    Generates random real numbers between 0 and 1 in a new column.
    :param result: Resulting column name
    """
    import random
    df[result] = [random.random() for _ in range(len(df))]  # Generate random numbers using Python's random module

    return df
