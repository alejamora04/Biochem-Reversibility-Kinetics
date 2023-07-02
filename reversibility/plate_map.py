# Loads and 384-well, & sample location into consolidated pandas dataframes
import os
import platform
import pandas as pd
import csv 

# File IO Iterate through specified directory to load specified files.
def get_file_paths(path, file_extension):
    file_paths = []
    current_os = platform.system()

    for root, dir, files in os.walk(path, topdown=False):
        for name in files:
            if file_extension in name:
                current_path = os.path.join(root, name)
                if current_os == "Linux":
                    linux_path = current_path.replace('\\', '/')
                    file_paths.append(linux_path)
                elif current_os == "Windows":
                    file_paths.append(current_path)
    print("[+] Retrieved all file paths using get_file_paths function for directory: ", path)
    return file_paths

# Parse all files within directory into list of names.
def get_file_names(file_path):
    file_names = []
    i = 0
    for file in file_path:
        current_file = file_path[i].split("\\")
        current_file = current_file[-1].split(".")
        current_file = current_file[0]
        file_names.append(current_file)
        i = i + 1 
    return file_names

# Turn CSV iterator into function
def csv_to_pandas(dataframe, start_position=0):
    condensed_list = []
    consolidated_list = []
    for column in dataframe:
        current_list = dataframe[column].values.tolist()
        condensed_list.append(current_list)

    for i in condensed_list[start_position:]:
        for j in i:
            consolidated_list.append(j)
    return consolidated_list

# INPUT: Read layout of 384 well plate format and sample locations into pandas df.
cwd = os.getcwd()
plate_path = "/input/plate-maps/"
plate_well_layout = os.join(cwd, plate_path)
file_ext = ".csv"

parsed_paths = get_file_paths(plate_well_layout, file_ext)
file_names = get_file_names(parsed_paths)

# Read Layout of 384 well plate and store it into pd Column
plate_well_layout = parsed_paths[0]
sample_layout = parsed_paths[1]

# OUTPUT: Write Output to CSV file 
out_path = 'output/csv/plate_map_output.csv'
file_out_path = os.path.join(cwd = out_path)

# Read sample position from 384-well plate into Pandas Df 
sample_location_df = pd.read_csv(sample_layout, header=None)
consolidated_sample_list = csv_to_pandas(sample_location_df, start_position=1)

well_layout_df = pd.read_csv(plate_well_layout, header=None)
consolidated_wells = csv_to_pandas(well_layout_df)

# Combine Multiple df into single indexed dataframe
plate_map_df = pd.DataFrame({"Compound": consolidated_sample_list, "Wells": consolidated_wells})

plate_map_df.to_csv(out_path)
print("[+] Plate_map.py has mapped the sample locations to the relevant wells.")