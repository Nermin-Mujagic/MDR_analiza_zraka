import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler



REGIJE_FILTER = {
    "SO2": {
        "regije": ["Koroška", "Osrednjeslovenska", "Posavska", "Savinjska", "Zasavska"],
        "zac_leto": "1997",
        "direktiva": "2005",
        "omejitev": 20
    },
    "PM10":{
        "regije":["Goriška", "Osrednjeslovenska", "Podravska", "Pomurska", "Posavska", "Savinjska", "Zasavska"],
        "zac_leto":"2002",
        "direktiva":"2005",
        "omejitev":40
    },
    "NO2": {
        "regije": ["Goriška", "Osrednjeslovenska", "Podravska", "Pomurska", "Savinjska", "Zasavska"],
        "zac_leto": "2002",
        "direktiva": "2010",
        "omejitev": 40,
    }
}

def filter_region_year(full_df: pd.DataFrame,snov="")->pd.DataFrame:
    df = full_df.copy()
    regije = REGIJE_FILTER[snov]["regije"]
    zac_leto = REGIJE_FILTER[snov]["zac_leto"]
    df = df.loc[(df['Regija'].isin(regije)) & (df['Datum'] >= zac_leto),["Regija","Datum",snov]]

    return df 


def lowerSumniki(word: str) -> str:
    word = word.strip()
    trans = str.maketrans("žŽčČšŠ", "zZcCsS")
    word = word.translate(trans)
    word = word.lower()
    return word


def simplifyColumn(df: pd.DataFrame, col: str, reg: bool) -> pd.DataFrame:
    df[col] = df[col].map(lowerSumniki, "ignore")

    if reg:
        df[col] = df[col].str.replace(r"\s*\(r\)\s*", "", regex=True)
        df[col] = df[col].str.replace("*", "")

    return df


def renamePostaja(df: pd.DataFrame) -> pd.DataFrame:
    first_col = df.columns[0]

    if first_col != "Postaja":
        df.rename(columns={first_col: "Postaja"}, inplace=True)

    return df

""" def detect_and_handle_outliers(df:pd.DataFrame, snov:str, threshold=3,handle_method='flag'):
    df_copy = df.copy()

    df_copy.loc[:,'Zscore'] = np.abs((df_copy[snov] - df_copy[snov].mean()) /df_copy[snov].std())

    outliers = df_copy[df_copy['Zscore'] > threshold]
    print(f"Number of outliers detected for {snov}: {len(outliers)}")
    print(outliers)

    match handle_method:
        case "flag":
            df_copy.loc[:,'Is_Outlier'] = df_copy['Zscore'] > threshold
        case "remove":
            df_copy = df_copy[df_copy['Zscore'] <= threshold]
            print("Outliers removed")
        case "replace":
            df_copy.loc[df_copy['Zscore']>threshold,snov] = np.nan
        case _:
            raise ValueError("Invalid handle_method. Must be 'flag', 'remove' or 'replace'")
        
    return df_copy """
