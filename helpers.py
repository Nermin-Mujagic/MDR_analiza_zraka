"""Various helper functions for reuse in jupyter notebooks"""

import pandas as pd


REGIJE_FILTER = {
    "SO2": {
        "regije": ["Koroška", "Osrednjeslovenska", "Posavska", "Savinjska", "Zasavska"],
        "zac_leto": "1997",
        "direktiva": "2005",
        "omejitev": 20,
    },
    "PM10": {
        "regije": [
            "Goriška",
            "Osrednjeslovenska",
            "Podravska",
            "Pomurska",
            "Posavska",
            "Savinjska",
            "Zasavska",
        ],
        "zac_leto": "2002",
        "direktiva": "2005",
        "omejitev": 40,
    },
    "NO2": {
        "regije": [
            "Goriška",
            "Osrednjeslovenska",
            "Podravska",
            "Pomurska",
            "Savinjska",
            "Zasavska",
        ],
        "zac_leto": "2002",
        "direktiva": "2010",
        "omejitev": 40,
    },
}

REGION_COLORS = {
    "Goriška": "skyblue",
    "Osrednjeslovenska": "lightcoral",
    "Podravska": "lightgreen",
    "Pomurska": "gold",
    "Posavska": "plum",
    "Savinjska": "lightseagreen",
    "Zasavska": "khaki",
    "Koroška": "lightsteelblue",  # Add Koroška
}


def filter_region_year(full_df: pd.DataFrame, snov="") -> pd.DataFrame:
    """
    Filters `full_df` by region and year based on `REGIJE_FILTER` for the given pollutant `snov`.

    Args:
        full_df (pd.DataFrame): Input DataFrame with air pollution data.
        snov (str): Pollutant to filter for (e.g., "SO2"). Must be in `REGIJE_FILTER`.

    Returns:
        pd.DataFrame: Filtered DataFrame with 'Regija', 'Datum', and `snov` columns.
    """
    df = full_df.copy()
    regije = REGIJE_FILTER[snov]["regije"]
    zac_leto = REGIJE_FILTER[snov]["zac_leto"]
    df = df.loc[
        (df["Regija"].isin(regije)) & (df["Datum"] >= zac_leto),
        ["Regija", "Datum", snov],
    ]

    return df


def lower_sumniki(word: str) -> str:
    """ removes šumniki and lowercases """
    word = word.strip()
    trans = str.maketrans("žŽčČšŠ", "zZcCsS")
    word = word.translate(trans)
    word = word.lower()
    return word


def simplify_column(df: pd.DataFrame, col: str, reg: bool) -> pd.DataFrame:
    """ removes unwanted characters and calls lower_sumniki """
    df[col] = df[col].map(lower_sumniki, "ignore")

    if reg:
        df[col] = df[col].str.replace(r"\s*\(r\)\s*", "", regex=True)
        df[col] = df[col].str.replace("*", "")

    return df


def rename_postaja(df: pd.DataFrame) -> pd.DataFrame:
    """ changes whatever first name of column into 'Postaja'"""
    first_col = df.columns[0]

    if first_col != "Postaja":
        df.rename(columns={first_col: "Postaja"}, inplace=True)

    return df
