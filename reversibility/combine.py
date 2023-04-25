# Merged the layout to the samples and readouts
import pandas as pd
import numpy as np
import csv

#[WORKS] Import Multiple dataframes and read them into memory
# Combine the formatted dataframes 
plate_path = "output/csv/load_samples_output.csv" 
readout_path = "output/csv/plate_map_output.csv"
samples_df = pd.read_csv(plate_path, index_col=[0])
readout_df = pd.read_csv(readout_path, index_col=[0])

# Validate df Format
# sample_preview = samples_df
# readout_preview = readout_df
print(f"Sample df preview: \n\n {samples_df}")
print(f"Readout df preview: \n\n {readout_df}")

#[WORKS] Join DataFrames by well and Assign compound name as 1st level index.
merged_1 = pd.merge(readout_df, samples_df, on="Well")
experiment_1 = merged_1.set_index(["Compound"])
print(f"Heres the Combination: \n\n {experiment_1}")

#[CHECKPOINT] Output Merged df into the output folder
out_path = "output/csv/combine_output.csv"
experiment_1.to_csv(out_path)
print("Operation combine.py Complete")

# TODO Build Pivot Table heirarchy based on Exp name and sample for more robust filtering options. 