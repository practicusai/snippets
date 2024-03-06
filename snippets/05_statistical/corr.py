from enum import Enum


class CorrMethods(str, Enum):
    pearson = "pearson"
    kendall = "kendall"
    spearman = "spearman"


def corr(df, numeric_col_list: list[str], corr_method: CorrMethods = CorrMethods.pearson):
    """
    Calculates the correlation of selected columns for each row separately.
    :param numeric_col_list: Columns with numeric values
    :param corr_method: Correlation method to use
    """
    df = df[numeric_col_list].corr(method=str(corr_method)).reset_index()

    return df
