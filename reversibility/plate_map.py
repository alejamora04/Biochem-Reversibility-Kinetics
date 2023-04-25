# Import and Read CSVs into pd Dataframes
import pandas as pd
import csv 

# [WORKS] Open sample plate csv from path
in_path = "/input/plate-maps/384_well.csv"
df = pd.read_csv(in_path)
preview = df.head
# Validate contents of df file
# print(preview)

# [WORKS] Iterate through each column adding samples to list skip 1st column
sample_list=[]
for column in df:
    samples = df[column].values.tolist()
    sample_list.append(samples)
# Validate parsed plate samples
# print(f"The Sample list is: \n \n {sample_list}')

# [WORKS] Loop through the list twice to consolidate values into single list
consolidated_list=[]
for i in sample_list[1:]:
    for j in i:
        consolidated_list.append(i)
# Validate Stacked List.
# print(f"The Stacked List is: \n \n {consolidated_list}")

# [WORKS] Populate Column 1 with Compound List
sample_column = {'Compound': consolidated_list}
sample_df = pd.DataFrame(sample_column)
# Validate plate in proper format
print(sample_df)

# [WORKS] Read Layout of 384 well plate and store it into pd Column
plate_path = "input/plate-data/sample-plate-csv"
well_layout_df = pd.read_csv(plate_path, header=None)
plate_preview = well_layout_df.head
# Validate format
# print(plate_preview)

# [WORKS] Iterate through each column adding samples to list
well_list=[]
for column in well_layout_df:
    samples = well_layout_df[column].values.tolist()
    well_list.append(samples)
# Validate format of parsed plate
# print(f"The wells in the plate are as follows: \n \n {well_list}")

# [WORKS] Loop through list twice to generate new pandas column
consolidated_wells=[]
for i in well_list:
    for j in i:
        consolidated_wells.append(j)
# Validate Stacked List
# print(f"The Wells in the plate are as follows: \n \n {consolidated_wells}")

# [WORKS] Convert list in Dictionary for pd Column
well_column = {'Well': consolidated_wells}
well_df = pd.DataFrame(well_column)
# Validate plate in proper format
print(well_df)

# [WORKS] Combine Multiple df into single indexed dataframe
protoype_df = pd.DataFrame({"Compound": consolidated_list, "wells": consolidated_wells})
print(f"The outgoing plate is in the following Format:.... \n \n {protoype_df}")

# [WORKS] Write Output to JSON or CSV file 
out_path = 'output/plate_map_output.csv'
df.to_csv(outpath)