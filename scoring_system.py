import pandas as pd
import itertools
import numpy as np


class ScoringSystem:
    def __init__(self, df: pd.DataFrame, snov: str):
        self.df = df
        self.snov = snov
        self.full_df = self.fill_df()

    def fill_df(self):
        # Extract all unique values
        regije = self.df["Regija"].unique()
        years = self.df["Leto"].unique()
        months = self.df["Mesec"].unique()
        cols = ["Regija", "Leto", "Mesec"]

        # Create all possible combinations
        cartesian = list(itertools.product(regije, years, months))
        cartesian = [row for row in cartesian]
        cart_df = pd.DataFrame(data=cartesian, columns=cols)

        missing_df = pd.merge(
            left=cart_df,
            right=self.df[cols].drop_duplicates(),
            on=cols,
            how="left",
            indicator=True,
        )
        missing_df = missing_df[missing_df["_merge"] == "left_only"].drop(
            columns="_merge"
        )
        missing_df[self.snov] = np.nan

        return pd.concat([self.df, missing_df])

    def pivot_counted(self, pd_counted: pd.DataFrame):
        return pd_counted.pivot_table(values="counts", index="Regija", columns="Leto")

    def region_score_months(self) -> pd.DataFrame:
        month_counts = (
            self.full_df.groupby(["Regija", "Leto"])[["Mesec", self.snov]]
            .apply(lambda x: (x[~x[self.snov].isna()]["Mesec"].nunique()))
            .reset_index(name="counts")
            .sort_values(by="Leto")
        )

        return self.pivot_counted(month_counts)

    def region_score_sources(self):
        source_counts = (
            self.full_df.groupby(["Regija", "Leto"])[["Mesec", self.snov]]
            .apply(lambda x: (x[~x[self.snov].isna()]["Mesec"].count()) / 12)
            .reset_index(name="counts")
            .sort_values(by="Leto")
        )

        return self.pivot_counted(source_counts)

    def calculate_total_score(self, alpha=1, beta=0.1):
        return alpha * self.region_score_months() + beta * self.region_score_sources()

    def optimal_year_range(self, min_regions=6, scale_factor=10):
        score_df = self.calculate_total_score()
        score_matrix = score_df.values
        years = np.array(score_df.columns)
        num_years = len(years)

        mean_region_score = np.mean(score_matrix[score_matrix > 0])
        year_weight = mean_region_score / scale_factor

        best_score = -np.inf
        best_range = (years[0], years[-1])
        best_regions = []
        

        for start_idx in range(num_years):
            for end_idx in range(start_idx, num_years):
                
                selected_scores = score_matrix[:, start_idx:end_idx + 1]
                year_range_length = end_idx - start_idx + 1

                valid_regions_mask = np.all(selected_scores > 0, axis=1)
                valid_scores = selected_scores[valid_regions_mask]
                num_valid_regions = np.sum(valid_regions_mask)

                if num_valid_regions >= min_regions:
                    total_score = np.sum(valid_scores)

                    adjusted_score = total_score + year_weight * (year_range_length ** 2)

                    if adjusted_score > best_score:
                        best_score = adjusted_score
                        best_range= (int(years[start_idx]), int(years[end_idx]))
                        best_regions = score_df.index[valid_regions_mask].to_list()
                

        return best_range, best_regions, best_score
