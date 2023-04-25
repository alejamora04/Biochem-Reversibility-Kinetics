# Open and import plate readout CSVs into pandas
import pandas as pd
import numpy as np
import csv 

# Cleans up plate readout CSVs 

# [WORKS] Open sample plate csv from path
in_path = "/input/plate-data/plate_readout.csv"
df = pd.read_csv(in_path)
# Drop Extraneous rows from plate data
plate_df.drop(index=[0:2], axis=0, inplace=True)
plate_df.drop(index=[384], axis=0, inplace=True)
preview = plate_df.head
# Validate contents of df file
# print(preview)

# [WORKS] Change Top Row of CSV for abs readout
list_label =[]
i=0
for i in range(0, 61):
    list_label.append("Abs_Min:"+ str(i))
    i = i+1
# Add "Well" label to first column
x = "Well"
list_label.insert(0, x)
# Validate layout
# print(f"The Time Series Row 1 label currenlty looks like: \n \n {list_label}')

# [WORKS] Assign List labels to columns
plate_df.columns=(list_label)
plate_df.index=np.arrange(384)
# Validate Layout.
# print(f"The current layout looks like: \n \n {plate_df}")

# [IN PROGRESS] Checkpoint - Test df Output
# Write dataframe to csv file in output folder 
out_path = 'output/load_samples_output.csv'
df.to_csv(outpath)