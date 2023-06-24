# Loads and 384-well, & sample location into consolidated pandas dataframes
import os
import pandas as pd
import csv 

# Read layout of 384 well plate format into pandas df.
cwd = os.getcwd()
plate_path = "/input/plate-maps/384_well.csv"
plate_well_layout = os.join(cwd, plate_path)
well_layout_df = pd.read_csv(plate_well_layout, header=none)

# Read Layout of 384 well plate and store it into pd Column
sample_path = "input/plate-data/sample-plate-csv"
sample_layout = os.join(cwd, sample_path)
sample_location_df = pd.read_csv(sample_layout, header=None)

# Validate contents of df file
print(sample_location_df.head)
print(well_layout_df.head)

# Iterate through each column adding samples to list
well_list=[]
for column in well_layout_df:
    samples = well_layout_df[column].values.tolist()
    well_list.append(samples)
# Validate format of parsed plate
# print(f"The wells in the plate are as follows: \n \n {well_list}")

# Loop through list twice to generate new pandas column
consolidated_wells=[]
for i in well_list:
    for j in i:
        consolidated_wells.append(j)
# Validate Stacked List
# print(f"The Wells in the plate are as follows: \n \n {consolidated_wells}")

# Convert list in Dictionary for pd Column
well_column = {'Well': consolidated_wells}
well_df = pd.DataFrame(well_column)
# Validate plate in proper format
print(well_df)

# Iterate through each column adding samples to list skip 1st column
sample_list=[]
for column in layout_df:
    samples = layout_df[column].values.tolist()
    sample_list.append(samples)
# Validate parsed plate samples
# print(f"The Sample list is: \n \n {sample_list}')

# Loop through the list twice to consolidate values into single list
consolidated_list=[]
for i in sample_list[1:]:
    for j in i:
        consolidated_list.append(j)
# Validate Stacked List.
# print(f"The Stacked List is: \n \n {consolidated_list}")

# Populate Column 1 with Compound List
sample_column = {'Compound': consolidated_list}
sample_df = pd.DataFrame(sample_column)
# Validate plate in proper format
print(sample_df)

# Combine Multiple df into single indexed dataframe
protoype_df = pd.DataFrame({"Compound": consolidated_list, "Wells": consolidated_wells})
print(f"The outgoing plate is in the following Format:.... \n \n {protoype_df}")

# Write Output to JSON or CSV file 
out_path = 'output/csv/plate_map_output.csv'
df.to_csv(out_path)
print("Operation plate_map.py is complete.")