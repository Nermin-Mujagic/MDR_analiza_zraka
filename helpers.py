import pandas as pd


def lowerSumniki(word: str) -> str:
    word = word.strip()
    trans = str.maketrans("žŽčČšŠ", "zZcCsS")
    word = word.translate(trans)
    word = word.lower()
    return word


def simplifyColumn(df: pd.DataFrame, col: str, reg: bool) -> pd.DataFrame:
    df[col] = df[col].map(lowerSumniki,'ignore')

    if reg:
        df[col] = df[col].str.replace(r"\s*\(r\)\s*", "", regex=True)
        df[col] = df[col].str.replace("*","")


    return df


def renamePostaja(df: pd.DataFrame)->pd.DataFrame:
    first_col = df.columns[0]

    if first_col != "Postaja":
        df.rename(columns={first_col: "Postaja"}, inplace=True)

    return df
