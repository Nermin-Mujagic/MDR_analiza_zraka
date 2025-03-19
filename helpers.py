import pandas as pd


def cleanPostaja(df: pd.DataFrame):
    df["Postaja"] = df["Postaja"].str.strip()

    trans = str.maketrans("žŽčČšŠ", "zZcCsS")
    df["Postaja"] = df["Postaja"].str.translate(trans)

    df["Postaja"] = df["Postaja"].str.lower()

    df["Postaja"] = df["Postaja"].str.replace(r"\s*\(r\)\s*", "", regex=True)

    return df


def renamePostaja(df: pd.DataFrame):
    first_col = df.columns[0]

    if first_col != "Postaja":
        df.rename(columns={first_col: "Postaja"}, inplace=True)

    return df


def lowerSumniki(word: str):
    trans = str.maketrans("žŽčČšŠ", "zZcCsS")
    word = word.translate(trans)
    word = word.lower()
    return word
