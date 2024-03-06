def slice_text(df, some_text_col: str, start: int, stop: int, step: int, result: str):
    """
    This function slices substrings from each element in the specified column of the DataFrame, using the specified start, stop, and step parameters.
    :param some_text_col: Name of the column containing text strings to be processed.
    :param start: Start position for the slice operation.
    :param stop: Stop position for the slice operation.
    :param step: Step size for the slice operation.
    :param result: Name of the resulting column containing the sliced substrings.
    """
    df[result] = df[some_text_col].str.slice(start, stop, step)

    return df
