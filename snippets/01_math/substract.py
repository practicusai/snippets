def substract(df, first_numeric_col: str, second_numeric_col: str | None, some_number: float | None, result: str):
    """
    Subtracts one column from another column, or subtracts a number from a column.
    Alternatively, it subtracts a specified number from each value in the first column.    
    
    :param first_numeric_col: The name of the column to subtract from.
    :param second_numeric_col: The name of the column to subtract (optional). If provided, each value in first_col will be subtracted from the corresponding value in second_col.
    :param some_number: The number to subtract (optional). If second_col is not provided, each value in first_col will be subtracted by this number.
    :param result: The name of the column where the resulting values will be stored.
    """
    if second_numeric_col:
        df[result] = df[first_numeric_col] - df[second_numeric_col]
    else:
        if some_number is None:
            raise ValueError("If a column is not selected, a number must be provided")

        import numpy as np
        df[result] = np.subtract(df[first_numeric_col], some_number)

    return df
