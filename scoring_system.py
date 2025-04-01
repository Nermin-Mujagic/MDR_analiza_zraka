import pandas as pd
from IPython.display import display  # Import display


class ScoringSystem:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.pollutant_cols = [
            col for col in df.columns if col not in ["Regija", "Leto", "Mesec"]
        ]

    def coverage_score(self) -> pd.DataFrame:
        """Calculates pollutant presence and displays the resulting DataFrame."""

        def check_pollutant_presence(group):
            presence_indicators = {}
            for col in self.pollutant_cols:
                if group[col].isnull().all():
                    presence_indicators[col] = 0
                else:
                    presence_indicators[col] = 1
            return pd.Series(presence_indicators)

        grouped = self.df.groupby(["Regija", "Leto", "Mesec"])
        pollutant_presence_df = grouped.apply(check_pollutant_presence).reset_index()

        return pollutant_presence_df

    def create_coverage_matrix(
        self, pollutant_presence_df: pd.DataFrame
    ) -> dict[str, pd.DataFrame]:
        """
        Creates a dictionary of region/year coverage matrices, one for each pollutant.

        Returns:
            dict: A dictionary where keys are pollutant names and values are DataFrames
                  with regions as rows, years as columns, and the sum of pollutant presence
                  indicators as values.
        """

        coverage_matrices = {}

        for pollutant in self.pollutant_cols:
            coverage_scores = pollutant_presence_df.groupby(['Regija','Leto'])[pollutant].sum().reset_index()

            coverage_matrix = coverage_scores.pivot(index='Regija', columns='Leto', values=pollutant)
            coverage_matrix = coverage_matrix.fillna(0)

            coverage_matrices[pollutant] = coverage_matrix

        return coverage_matrices
    

    def find_best_coverage_range_pollutant_specific(self, coverage_matrix:pd.DataFrame, min_coverage:float=10.0):
        """
        Finds the best year range and regions with coverage >= min_coverage,
        using a Pareto frontier approach to balance time range length and
        number of regions covered.

        Args:
            coverage_matrix (pd.DataFrame): The coverage matrix for a specific pollutant.
            min_coverage (float): Minimum coverage score (e.g., 10.0 for 10 months).

        Returns:
            tuple: (start_year, end_year, list_of_regions)
        """
        

        
            




    
    



