import enum
import numpy as np
import pandas as pd
import copy


def cumulative_to_new(csv_in: str, csv_out: str):

    pd.options.mode.chained_assignment = None  # default='warn'. Turn off pandas warning.

    all_data = pd.read_csv(csv_in)  # Read in the original csv data.

    final_data = pd.DataFrame()  # Initialize final edited data frame.

    # For every state, for every county, populate New Cases and New Deaths.
    # Create thise field by progressively diffing Cumulative stats.
    for state in list(np.unique(all_data.State)):
        state_data = all_data.loc[all_data.State == state]  # Filter data to only relevant state.

        for county in list(np.unique(state_data.County)):
            county_data = state_data.loc[state_data.County == county]  # Filter data to only relevant county.

            sorted_county_data = county_data.sort_values(by=['Date'], ascending=True)  # Sort by date.

            num_rows = sorted_county_data.shape[0]
            for i in range(num_rows):  # For every county, turn cumulative into "new".

                if i == 0:  # First entry in time cumulative == new, so no change.
                    sorted_county_data["New Cases"].iloc[i] = sorted_county_data["Cumulative Cases"].iloc[i]
                    sorted_county_data["New Deaths"].iloc[i] = sorted_county_data["Cumulative Deaths"].iloc[i]

                else:  # Diff current with previous to get "new" cases.
                    new_cases = (sorted_county_data["Cumulative Cases"].iloc[i]
                        - sorted_county_data["Cumulative Cases"].iloc[i-1])
                    
                    if new_cases < 0:  # For weird negative new cases, just reset to zero.
                        new_cases = 0
                    
                    sorted_county_data["New Cases"].iloc[i] = new_cases  # Add new cases to dataframe.

                    new_deaths = (sorted_county_data["Cumulative Deaths"].iloc[i]
                        - sorted_county_data["Cumulative Deaths"].iloc[i-1])
                    
                    if new_deaths < 0:  # For weird negative new deaths, just reset to zero.
                        new_deaths = 0
                    
                    sorted_county_data["New Deaths"].iloc[i] = new_deaths
                    
            final_data = pd.concat([final_data, sorted_county_data])  # Concat results.
            
        print(f'Finished {state}.')  # Progress marker.

    final_data.to_csv(csv_out, index=False)  # Write data to new csv.
