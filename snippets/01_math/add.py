def add(df, first_numeric_col: str, second_numeric_col: str | None, some_number: float | None, result: str):
    """
    Adds values from one or two columns, or a column with a number, and adds the result as a new column to the DataFrame.
    :param first_numeric_col: Name of the first column to be added.
    :param second_numeric_col: (Optional) Name of the second column to be added. If None, some_number must be provided.
    :param some_number: (Optional) A number to be added to the values in the first column. Required if second_col is None.
    :param result: Name of the resulting column where the addition results will be stored.
    """
    if second_numeric_col:
        df[result] = df[first_numeric_col] + df[second_numeric_col]
    else:
        if some_number is None:
            raise ValueError("If a column is not selected, a number must be provided")

        import numpy as np
        df[result] = np.add(df[first_numeric_col], some_number)

    return df
