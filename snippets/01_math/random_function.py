def random_function(df, result: str):
    """
    Generates random real numbers between 0 and 1 in a new column.
    :param result: Name of the resulting column where the generated random numbers will be stored.
    """
    import random
    df[result] = [random.random() for _ in range(len(df))]  # Generate random numbers using Python's random module

    return df
