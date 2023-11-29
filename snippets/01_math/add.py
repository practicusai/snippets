def add(df, some_col: str, add_col: str | None, some_number: object | None, new_col: str):
    if add_col:
        df[new_col] = df[some_col] + df[add_col]
    else:
        assert some_number is not None, "If a column is not selected, a number must be provided"
        df[new_col] = df[some_col] + some_number

    return df
