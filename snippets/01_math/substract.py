def substract(df, first_col: str, second_col: str | None, some_number: float | None, result: str):
    """
    Subtracts a column from another column, or from a number.
    :param first_col: First column to subtract from
    :param second_col: Second column to subtract
    :param some_number: Some number to subtract
    :param result: Resulting column name
    """
    if second_col:
        df[result] = df[first_col] - df[second_col]
    else:
        if some_number is None:
            raise ValueError("If a column is not selected, a number must be provided")

        import numpy as np
        df[result] = np.subtract(df[first_col], some_number)

    return df
