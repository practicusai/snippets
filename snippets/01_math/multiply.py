def multiply(df, first_col: str, second_col: str | None, some_number: float | None, result: str):
    """
    Multiplies a column with another column, or with a number.
    :param first_col: First column
    :param second_col: Second column
    :param some_number: Some number
    :param result: Resulting column name
    """
    if second_col:
        df[result] = df[first_col] * df[second_col]
    else:
        if some_number is None:
            raise ValueError("If a column is not selected, a number must be provided")

        import numpy as np
        df[result] = np.multiply(df[first_col], some_number)

    return df
