# Merged the layout to the samples and readouts
import pandas as pd
import numpy as np
import csv
import os

# Import Multiple dataframes and read them into memory 
cwd = os.getcwd()
plate_path = "output/csv/load_samples_output.csv" 
readout_path = "output/csv/plate_map_output.csv"
in_plate_path = os.join(cwd, plate_path)
in_readout_path = os.join(cwd, readout_path)
samples_df = pd.read_csv(in_plate_path, index_col=[0])
readout_df = pd.read_csv(in_readout_path, index_col=[0])

# Validate df Format
print(f"Sample df preview: \n\n {samples_df}")
print(f"Readout df preview: \n\n {readout_df}")

# Join DataFrames by well and Assign compound name as 1st level index.
merged_1 = pd.merge(readout_df, samples_df, on="Well")
experiment_1 = merged_1.set_index(["Compound"])
print(f"Heres the Combination: \n\n {experiment_1}")

#[CHECKPOINT] Output Merged df into the output folder
out_path = "output/csv/combine_output.csv"
experiment_1.to_csv(out_path)
print("[+] Combine.py has finished combining the data from both csv files.")

# TODO Build Pivot Table heirarchy based on Exp name and sample for more robust filtering options. 