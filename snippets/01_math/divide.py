def divide(df, first_numeric_col: str, second_numeric_col: str | None, some_number: float | None, result: str):
    """
    Divides the values in a specified column by another column or by a number, and adds the result as a new column to the DataFrame.
    :param first_numeric_col: Name of the first column whose values are to be divided.
    :param second_numeric_col: Name of the second column to divide by. Optional, defaults to None.
                               If None, `some_number` must be provided.
    :param some_number: Some number to divide by. Optional, defaults to None.
                        If None, `second_col` must be provided.
    :param result: Name of the resulting column where the division results will be stored.
    """
    if second_numeric_col:
        df[result] = df[first_numeric_col] / df[second_numeric_col]
    else:
        if some_number is None:
            raise ValueError("If a column is not selected, a number must be provided")

        import numpy as np
        df[result] = np.divide(df[first_numeric_col], some_number)

    return df
