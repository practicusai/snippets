def multiply(df, first_numeric_col: str, second_numeric_col: str | None, some_number: float | None, result: str):
    """
    Multiplies a column with another column, or with a number.
    :param first_col: Name of the first column to multiply.
    :param second_col: Name of the second column to multiply.
                       If provided, values in this column will be multiplied with `first_col`.
    :param some_number: Some number to multiply with `first_col`.
                        If `second_col` is not provided, `first_col` will be multiplied with this number.
    :param result: Name of the resulting column where the multiplied values will be stored.
    """
    if second_numeric_col:
        df[result] = df[first_numeric_col] * df[second_numeric_col]
    else:
        if some_number is None:
            raise ValueError("If a column is not selected, a number must be provided")

        import numpy as np
        df[result] = np.multiply(df[first_numeric_col], some_number)

    return df
